from flask import render_template, flash, request, Blueprint
from datetime import datetime
from flask import redirect, url_for, session
from blueprints.forms_admin import LoginForm, PwdForm, ScenicForm, AreaForm, TravelsForm
from models import Admin, Adminlog, Area, Scenic, Oplog, Travels, UserLog, User, Suggestion
from functools import wraps
from extendsions import db
from werkzeug.utils import secure_filename
from config import UP_DIR
import random
import os
import uuid
from flask_ckeditor import upload_success, upload_fail
from sqlalchemy import or_

admin_bp = Blueprint("admin", __name__, url_prefix="/admin")


# 是否登录
def admin_login(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if "admin" not in session:
            return redirect(url_for("admin.login"))
        return func(*args, **kwargs)
    return decorated_function


# 添加数据库操作日志功能
def add_oplog(reason):
    oplog = Oplog(
        admin_id=session["admin_id"],
        ip=request.remote_addr,                            # 获取当前ip
        reason=reason
    )
    db.session.add(oplog)
    db.session.commit()


# 唯一文件名无后缀
def gen_rnd_filename():
    return datetime.now().strftime("%Y%m%d%H%M%S") + str(uuid.uuid4().hex)


# 唯一文件名加后缀
def change_filename(filename):
    """
    传入原文件名
    返回新的唯一文件名
    """
    fileinfo = os.path.splitext(filename)
    filename = gen_rnd_filename() + fileinfo[-1]
    return filename


@admin_bp.route("/")
@admin_login
def index():
    """
    后台首页介绍
    """
    return render_template("admin/index.html")


@admin_bp.route("/login/", methods=["GET", "POST"])
def login():
    """
    后台登录
    """
    form = LoginForm()
    if form.validate_on_submit():
        data = form.data
        admin = Admin.query.filter_by(name=data["name"]).first()
        if not admin.check_pwd(data["pwd"]):
            flash("密码错误!", "err")                                # 闪存错误信息
            return redirect(url_for("admin.login"))                # 跳转到后台登录页
        session["admin"] = data["name"]
        session["admin_id"] = admin.id
        admin_log = Adminlog(
            admin_id=admin.id,
            ip=request.remote_addr,
        )
        db.session.add(admin_log)
        db.session.commit()
        return redirect(url_for("admin.index"))                    # 返回后台主页
    return render_template("admin/login.html", form=form)


@admin_bp.route('/logout/')
@admin_login
def logout():
    """
    后台注销登录
    """
    session.pop("admin", None)
    session.pop("admin_id", None)
    return redirect(url_for("admin.login"))


@admin_bp.route('/pwd/', methods=["GET", "POST"])
@admin_login
def pwd():
    """
    后台密码修改
    """
    form = PwdForm()
    if form.validate_on_submit():                                   # post请求，并且旧密码验证以及其他差错验证通过
        data = form.data                                            # 接收表单数据
        admin = Admin.query.filter_by(name=session["admin"]).first()  # 查询数据库账户
        from werkzeug.security import generate_password_hash          # 导入 werkzeug的密码 加密保存功能
        admin.pwd = generate_password_hash(data["new_pwd"])           # 加密新密码
        db.session.add(admin)                                         # 加入数据库会话
        db.session.commit()                                           # 提交数据库，修改数据
        flash("修改密码成功，请重新登录！", "ok")                           # flash存储修改成功消息
        return redirect(url_for('admin.logout'))                      # 跳转后台登录界面
    if request.method == "post" and (not form.validate()):
        flash("修改失败！", "err")
    return render_template("admin/pwd.html", form=form)               # 渲染模板


@admin_bp.route('/scenic/add/', methods=["GET", "POST"])
@admin_login
def scenic_add():
    """
    景区添加
    """
    form = ScenicForm()                                                     # 实例化form表单
    area_dict = [(-1, "无所属地区")]                                          # 后台页面加个选项，数据库area_id空
    for v in Area.query.all():                                              # 查询数据库已添加的地区
        area_dict.append((v.id, v.name))                                    # 地区id：地区名称
    form.area_id.choices = area_dict                                        # 为form表单的area_id添加choices
    # print("------------form.area_id.choices-----------")
    # print(form.area_id.choices)
    if form.validate_on_submit():                                           # 表单post提交，后台验证成功
        data = form.data                                                    # 接收表单数据
        scenic_count = Scenic.query.filter_by(title=data["title"]).count()  # 景区是否存在（None不报错）
        if scenic_count == 1:                                               # 景区已存在
            flash("景区名称已经存在！", "err")                                  # 存储错误消息
            return redirect(url_for('admin.scenic_add'))                    # 重新渲染模板

        file_secure_name = secure_filename(data["logo"].filename)
        filename = change_filename(file_secure_name)               # 唯一文件名加后缀（函数）
        file_path = UP_DIR + filename                              # 从config 拿封面图片上传的保存根路径，拼接
        # print("景区添加的logo保存路径：%s" % file_path)
        dirname = os.path.dirname(file_path)                       # 上级目录路径
        if not os.path.exists(dirname):                            # 不存在则创建目录
            os.makedirs(dirname)
        data["logo"].save(file_path)                               # 保存图片到指定路径下

        # 为Scenic类实例属性赋值，写入一条数据到数据库
        # print("---------data[area_id]-------")
        # print(data["area_id"])
        scenic = Scenic(
            title=data["title"],
            logo=filename,
            star=int(data["star"]),
            address=data["address"],
            is_hot=int(data["is_hot"]),
            is_recommended=int(data["is_recommended"]),
            area_id=None if data["area_id"] == -1 else data["area_id"],
            introduction=data["introduction"],
            content=data["content"],
        )
        db.session.add(scenic)                                         # 添加数据
        db.session.commit()                                            # 提交数据
        flash("添加景区成功！", "ok")                                     # 使用flash保存添加成功信息
        add_oplog("添加景区" + data["title"])                            # 添加操作类型日志
        return redirect(url_for('admin.scenic_add'))                   # 页面可跳转，此处是重新渲染
    return render_template("admin/scenic_add.html", form=form)         # 渲染模板


@admin_bp.route('/scenic/list/', methods=["GET"])
@admin_login
def scenic_list():
    """
    景区列表页面
    """
    title = request.args.get('titleSearch', '', type=str)                      # 获取查询标题
    if title:
        scenic_all = Scenic.query.filter_by(title=title).order_by(
            Scenic.addtime.desc()                                              # 根据添加时间降序查询结果
        )
    else:
        scenic_all = Scenic.query.all()
    return render_template("admin/scenic_list.html", scenic_all=scenic_all)   # 渲染模板


@admin_bp.route('/scenic/del/<int:scenic_id>/', methods=["GET"])
@admin_login
def scenic_del(scenic_id=None):
    """
    景区删除
    """
    scenic = Scenic.query.filter_by(id=int(scenic_id)).first()        # 根据景区ID查找数据
    db.session.delete(scenic)                                         # 删除数据
    db.session.commit()                                               # 提交数据
    flash("景区删除成功", "ok")                                          # 使用flash存储成功信息
    add_oplog("删除景区" + scenic.title)                                # 添加日志
    return redirect(url_for('admin.scenic_list'))                     # 渲染模板


@admin_bp.route("/scenic/edit/<int:id>/", methods=["GET", "POST"])
@admin_login
def scenic_edit(id=None):
    """
    景区编辑页面
    """
    form = ScenicForm()                                             # 实例化ScenicForm类
    area_dict = [(-1, "无所属地区")]                                # 后台页面添加一条选择，数据库area_id为空
    for v in Area.query.all():                                      # 数据库查询已添加的  地区id：地区名称
        area_dict.append((v.id, v.name))
    form.area_id.choices = area_dict                               # 为表单的area_id添加choices选项
    form.submit.label.text = "修改"                                 # 修改提交按钮的文字
    scenic = Scenic.query.filter_by(id=int(id)).first()            # 根据传入的景区id到数据库中查找
    form.logo.validators = []                                      # logo图片文件上传校验为空
    if request.method == "GET":                                    # 如果以GET方式提交，获取景区信息
        form.title.data = scenic.title                             # 预置选择
        form.star.data = scenic.star
        form.introduction.data = scenic.introduction
        form.content.data = scenic.content
        form.address.data = scenic.address
        form.is_hot.data = scenic.is_hot
        form.is_recommended.data = scenic.is_recommended
        form.area_id.data = scenic.area_id if scenic.area_id else '-1'  # 数据库area_id空则赋 -1
        print("--------form.area_id--------")
        print(form.area_id.data)

    if form.validate_on_submit():                                                # post提交并验证成功
        data = form.data                                                         # form表单数据
        if data["title"] != scenic.title:                                        # 修改了景区名
            scenic_count = Scenic.query.filter_by(title=data["title"]).count()   # 景区名是否已存在
            if scenic_count == 1:                                                # 如果重复存在
                flash("景点名称已经存在！", "err")                                   # 存储错误消息
                return redirect(url_for('admin.scenic_edit', id=id))             # 重新渲染当前页面
        print("---------上传新logo吗？----------")
        if data['logo'].filename != "":                                          # 判断是否重新上传了logo图片
            print("------重新上传logo图片-----")
            file_secure_name = secure_filename(data["logo"].filename)
            random_num = random.randint(0, 100)
            filename = datetime.now().strftime("%Y%m%d%H%M%S") + "_" + str(random_num) + "." + file_secure_name.rsplit('.', 1)[-1]
            filepath = UP_DIR + filename                              # 从config 拿封面图片上传的根路径，拼接
            dirname = os.path.dirname(filepath)                       # 上层路径
            if not os.path.exists(dirname):                           # 上层路径没有则创建路径目录
                os.makedirs(dirname)
            data["logo"].save(filepath)                               # 保存图片到指定路径下
            scenic.logo = filename                                    # 准备数据，logo文件名写入数据库
        # 为Scenic数据库类实例属性赋值，写入数据库
        # print("---------data[area_id]-------")
        # print(data["area_id"])
        scenic.title = data["title"]
        scenic.address = data["address"]
        scenic.area_id = None if data["area_id"] == -1 else data["area_id"]
        scenic.star = int(data["star"])
        scenic.is_hot = int(data["is_hot"])
        scenic.is_recommended = int(data["is_recommended"])
        scenic.introduction = data["introduction"]
        scenic.content = data["content"]

        db.session.add(scenic)                                                   # 添加数据会话
        db.session.commit()                                                      # 提交数据库
        flash("修改景区成功！", "ok")                                               # 存储成功消息
        add_oplog("修改景区" + data["title"])
        return redirect(url_for('admin.scenic_edit', id=id))                     # 重新渲染
    return render_template("admin/scenic_edit.html", form=form, scenic=scenic)   # 渲染模板，传递变量


@admin_bp.route('/area/add/', methods=["GET", "POST"])
@admin_login
def area_add():
    """
    地区添加
    """
    form = AreaForm()                                                       # 实例化form表单
    if form.validate_on_submit():                                           # 表单post提交，成功
        data = form.data                                                    # 接收表单数据
        area_count = Area.query.filter_by(name=data["name"]).count()        # 地区是否存在（None不报错）
        if area_count == 1:                                                 # 地区标题已存在
            flash("地区标题已经存在！", "err")                                  # 存储错误消息
            return redirect(url_for('admin.area_add'))                      # 重新渲染模板

        # 为Area类实例属性赋值，写入数据库
        area = Area(
            name=data["name"],
            is_recommended=int(data["is_recommended"]),
            introduction=data["introduction"],
        )
        db.session.add(area)                                              # 添加数据
        db.session.commit()                                               # 提交数据
        flash("添加地区成功！", "ok")                                        # 使用flash保存添加成功信息
        add_oplog("添加地区" + data["name"])                                # 添加提交数据库中的日志
        return redirect(url_for('admin.area_add'))                        # 页面可跳转，此处是重新渲染
    return render_template("admin/area_add.html", form=form)              # 渲染模板


@admin_bp.route('/area/list/', methods=["GET"])
@admin_login
def area_list():
    """
    地区列表页面
    """
    name = request.args.get('nameSearch', '', type=str)                      # 查询地区标题
    if name:
        area_all = Area.query.filter_by(name=name).order_by(
            Area.addtime.desc()                                             # 根据添加时间降序查询结果
        )
    else:
        area_all = Area.query.all()
    return render_template("admin/area_list.html", area_all=area_all)       # 渲染模板


@admin_bp.route('/area/del/<int:id>/', methods=["GET"])
@admin_login
def area_del(id=None):
    """
    地区删除
    """
    # filter_by在查不到或多个的时候并不会报错，get会报错。
    area = Area.query.filter_by(id=id).first_or_404()
    db.session.delete(area)
    db.session.commit()
    add_oplog("删除地区" + area.name)                                    # 添加操作日志
    flash("地区<<{0}>>删除成功".format(area.name), "ok")
    return redirect(url_for("admin.area_list"))


@admin_bp.route("/area/edit/<int:id>/", methods=["GET", "POST"])
@admin_login
def area_edit(id=None):
    """
    地区编辑页面
    """
    form = AreaForm()                                                           # 实例化AreaForm类
    form.submit.label.text = "修改"                                              # 修改提交按钮的文字
    area = Area.query.filter_by(id=int(id)).first()                    # 根据传入的景区id到数据库中查找

    if request.method == "GET":                                        # 如果以GET方式提交，获取景区信息
        form.name.data = area.name
        form.introduction.data = area.introduction
        form.is_recommended.data = area.is_recommended

    if form.validate_on_submit():                                      # post提交并验证成功
        data = form.data                                               # form表单数据
        if data["name"] != area.name:                                  # 修改了景区名
            area_count = area.query.filter_by(name=data["name"]).count()  # 景区名是否已存在
            if area_count == 1:                                         # 如果重复存在
                flash("地区名称已经存在！", "err")                          # 存储错误消息
                return redirect(url_for('admin.area_edit', id=id))      # 重新渲染当前页面
        # 为Area数据库类area实例属性重新赋值，写入数据库
        area.name = data["name"]
        area.introduction = data["introduction"]
        area.is_recommended = int(form.data["is_recommended"])

        db.session.add(area)                                            # 添加数据会话
        db.session.commit()                                             # 提交数据库
        flash("修改地区成功！", "ok")                                      # 存储成功消息
        import datetime
        add_oplog("修改地区" + data["name"])
        return redirect(url_for('admin.area_edit', id=id))                # 重新渲染
    return render_template("admin/area_edit.html", form=form, area=area)  # 渲染模板


@admin_bp.route("/travels/add/", methods=["GET", "POST"])
@admin_login
def travels_add():
    """
    添加游记
    """
    form = TravelsForm()                                                      # 实例化游记表表单
    scenic_dict = [(-1, "无所属景区")]                                    # 后台页面加个选项，数据库area_id空
    for v in Scenic.query.all():                                              # 查询数据库已添加的地区
        scenic_dict.append((v.id, v.title))                                   # 景区id：地区名称
    form.scenic_id.choices = scenic_dict                                # 为form表单的area_id添加choices
    if form.validate_on_submit():                                             # 表单post，提交成功
        data = form.data                                                      # 表单数据
        travels_count = Travels.query.filter_by(title=data["title"]).count()  # 查询游记标题
        if travels_count == 1:                                                # 标题有重复数据。
            flash("景点已经存在！", "err")
            return redirect(url_for('admin.travels_add'))
        travels = Travels(
            title=data["title"],
            author=data["author"],
            scenic_id=None if data["scenic_id"] == -1 else data["scenic_id"],
            content=data["content"],
        )
        db.session.add(travels)
        db.session.commit()
        add_oplog("添加游记" + data["title"])                                    # 添加日志
        flash("添加游记成功！", "ok")
        return redirect(url_for('admin.travels_add'))
    return render_template("admin/travels_add.html", form=form)


@admin_bp.route("/travels/list/", methods=["GET"])
@admin_login
def travels_list():
    """
    景区列表页面
    """
    title_search = request.args.get('titleSearch', '', type=str)
    if title_search:
        # 使用like实现模糊查询
        travels_all = Travels.query.filter(Travels.title.like("%" + title_search + "%")).order_by(
            Travels.addtime.desc())
    else:
        travels_all = Travels.query.order_by(
            Travels.addtime.desc()
        )
    return render_template("admin/travels_list.html", travels_all=travels_all)


@admin_bp.route("/travels/edit/<int:id>/", methods=["GET", "POST"])
@admin_login
def travels_edit(id=None):
    """
    编辑游记
    """
    form = TravelsForm()
    form.scenic_id.choices = [(v.id, v.title) for v in Scenic.query.all()]
    scenic_dict = [(-1, "无所属地区")]                             # 后台页面添加一条选择，数据库scenic_id为空
    for v in Scenic.query.all():                                 # 数据库查询已添加的  景区id：景区名称title
        scenic_dict.append((v.id, v.title))
    form.scenic_id.choices = scenic_dict                         # 为表单的scenic_id添加choices选项
    form.submit.label.text = "修改"                               # 修改提交按钮的文字
    form.submit.label.text = "修改"
    travels = Travels.query.get_or_404(int(id))
    if request.method == "GET":
        form.scenic_id.data = travels.scenic_id
        form.content.data = travels.content
        form.author.data = travels.author
        form.title.data = travels.title
    if form.validate_on_submit():
        data = form.data
        # 判断是否有重复数据
        if travels.title != data["title"]:
            travels_count = Travels.query.filter_by(title=data["title"]).count()
            if travels_count == 1:
                flash("游记名称已经存在！", "err")
                return redirect(url_for('admin.travels_edit', id=id))
        # 修改数据
        travels.title = data["title"]
        travels.scenic_id = None if data["scenic_id"] == -1 else data["scenic_id"]
        travels.author = data["author"]
        travels.content = data["content"]
        # 加入数据库会话，提交，后台页面返回操作成功提示
        db.session.add(travels)
        db.session.commit()
        flash("修改景区成功！", "ok")
        return redirect(url_for('admin.travels_edit', id=id))
    return render_template("admin/travels_edit.html", form=form, travels=travels)


@admin_bp.route("/travels/del/<int:id>/", methods=["GET"])
@admin_login
def travels_del(id=None):
    """
    景区删除
    """
    travels = Travels.query.get_or_404(id)
    db.session.delete(travels)
    db.session.commit()
    flash("游记删除成功", "ok")
    add_oplog("删除游记" + travels.title)                                      # 添加操作日志
    return redirect(url_for('admin.travels_list'))


@admin_bp.route("/oplog/list/", methods=["GET"])
@admin_login
def oplog_list():
    """
    操作日志列表
    """
    oplog_data = Oplog.query.filter().order_by(Oplog.addtime.desc())
    print("------------oplog_data---------")
    print(oplog_data)
    return render_template("admin/oplog_list.html", oplog_data=oplog_data)


@admin_bp.route("/adminloginlog/list/", methods=["GET"])
@admin_login
def adminloginlog_list():
    """
    管理员登录日志列表
    """
    loginlog_data = Adminlog.query.filter().order_by(Adminlog.addtime.desc())                                                                # 联表
    return render_template("admin/adminloginlog_list.html", loginlog_data=loginlog_data)


@admin_bp.route("/userloginlog/list/", methods=["GET"])
@admin_login
def userloginlog_list():
    """
    会员登录日志列表
    """
    loginlog_data = UserLog.query.filter().order_by(UserLog.addtime.desc())
    return render_template("admin/userloginlog_list.html", loginlog_data=loginlog_data)


@admin_bp.route("/user/list/", methods=["GET"])
@admin_login
def user_list():
    """
    会员列表
    """
    title_email_search = request.args.get('title_email_Search', '', type=str)
    filters = or_(User.username == title_email_search, User.email == title_email_search)
    if title_email_search and filters:
        # 根据姓名或者邮箱查询
        user_data = User.query.filter(filters).order_by(User.addtime.desc())
    else:
        user_data = User.query.order_by(User.addtime.desc())
    return render_template("admin/user_list.html", user_data=user_data)


@admin_bp.route("/user/view/<int:id>/", methods=["GET"])
@admin_login
def user_view(id=None):
    """
    查看会员详情
    """
    user = User.query.get_or_404(int(id))
    return render_template("admin/user_view.html", user=user)    # 用户头像功能未写，图片写死


@admin_bp.route("/user/del/<int:id>/", methods=["GET"])
@admin_login
def user_del(id=None):
    """
    删除会员
    """
    user = User.query.get_or_404(int(id))
    db.session.delete(user)
    db.session.commit()
    add_oplog("删除会员"+user.username)                                        # 添加日志
    flash("删除会员成功！", "ok")
    return redirect(url_for('admin.user_list'))


@admin_bp.route("/suggestion_list/", methods=["GET"])
@admin_login
def suggestion_list():
    """
    意见建议列表
    """
    name_email_search = request.args.get('name_email_Search', '', type=str)
    if name_email_search:
        # 根据昵称或者邮箱查询
        filters = or_(Suggestion.name == name_email_search, User.email == name_email_search)
        suggestion_data = Suggestion.query.filter(filters).order_by(Suggestion.addtime.desc())
    else:
        suggestion_data = Suggestion.query.order_by(Suggestion.addtime.desc())
    return render_template("admin/suggestion_list.html", suggestion_data=suggestion_data)


@admin_bp.route("/suggestion/del/<int:id>/", methods=["GET"])
@admin_login
def suggestion_del(id=None):
    """
    删除建议
    """
    suggestion = Suggestion.query.get_or_404(int(id))
    db.session.delete(suggestion)
    db.session.commit()
    add_oplog("删除意见建议")                                                   # 添加日志
    flash("删除成功！", "ok")
    return redirect(url_for('admin.suggestion_list'))


# 允许上传的文件，以及文件格式校验
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ['png', 'jpg', 'jpeg', 'gif']


# handle image upload for ckeditor
@admin_bp.route('/ckupload/', methods=['POST'])
@admin_login
def ckupload():
    """
    富文本编辑器的图片上传，图片文件名处理
    """
    f = request.files.get('upload')                        # 富文本编辑器提交的数据对象
    if not allowed_file(f.filename):                       # 如果不含"."格式或图片格式不支持，上传图片失败
        return upload_fail('Image only!')
    my_name, fext = os.path.splitext(f.filename)
    rnd_name = '%s%s' % (gen_rnd_filename(), fext)
    filepath = os.path.join(UP_DIR, 'ckeditor', rnd_name)
    dirname = os.path.dirname(filepath)                                          # 上级目录路径
    if not os.path.exists(dirname):                                              # 不存在则创建目录
        os.makedirs(dirname)
    f.save(filepath)                                                             # 保存图片到服务器
    url = url_for('static', filename='%s/%s' % ('uploads/ckeditor', rnd_name))
    return upload_success(url, f.filename)
