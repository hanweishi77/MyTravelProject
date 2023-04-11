# _*_ codding:utf-8 _*_
"""网页用户界面视图函数"""
# 该注释是我在测试git的功能
from flask import request, render_template, flash, redirect, url_for, session
from blueprints.forms import RegisterForm, LoginForm, SuggetionForm
from flask import Blueprint
from models import User, UserLog, Area, Scenic, Collect, Travels, Suggestion
from extendsions import db
from werkzeug.security import generate_password_hash
from sqlalchemy import and_
from functools import wraps

# 创建蓝home_bp
home_bp = Blueprint("home", __name__, url_prefix="/")


def user_login(func):
    """
    登录装饰器
    """
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if "user_id" not in session:
            return redirect(url_for("home.login"))
        return func(*args, **kwargs)
    return decorated_function


@home_bp.route("/")
def index():
    """
    首页
    """
    area = Area.query.all()                                                     # 获取所有地区
    hot_area = Area.query.filter_by(is_recommended=1).limit(2).all()            # 获取热门区域
    scenic = Scenic.query.filter_by(is_hot=1).all()                             # 热门景区
    return render_template("home/index.html", area=area, hot_area=hot_area, scenic=scenic)  # 渲染模板


@home_bp.route("/login/", methods=["GET", "POST"])
def login():
    """登录"""
    form = LoginForm()
    if form.validate_on_submit():
        data = form.data
        user = User.query.filter_by(email=data["email"]).first()
        if not user.check_pwd(data["pwd"]):
            flash("密码错误", "err")
            return redirect(url_for("home.login"))
        session["email"] = data["email"]                             # 将email写入session
        session["user_id"] = user.id                                 # 将user_id写入session, 后面用户判断用户是否登录
        userlog = UserLog(                                           # 将用户登录信息写入Userlog表
            user_id=user.id,
            ip=request.remote_addr
        )
        db.session.add(userlog)                                      # 存入数据
        db.session.commit()                                          # 提交数据
        return redirect(url_for("home.index"))                       # 登录成功，跳转到首页
    return render_template("home/login.html", form=form)


@home_bp.route("/register/", methods=["GET", "POST"])
def register():
    """
    用户注册功能
    """
    form = RegisterForm()                                                # 导入注册表单
    if request.method == "GET":
        return render_template("home/register.html", form=form)
    else:
        if form.validate():                                              # 表单验证成功
            data = form.data
            user = User(
                username=data["username"],
                email=data["email"],
                pwd=generate_password_hash(data["pwd"]),
            )
            db.session.add(user)                                         # 添加数据
            db.session.commit()                                          # 提交数据库
            flash("注册成功,前去登录", "ok")                                 # 使用flask存储成功信息
            return redirect(url_for("home.login"))
        else:                                                            # 表单验证失败
            print(form.errors)
            return render_template("home/register.html", form=form)


@home_bp.route("/logout/")
def logout():
    """退出登录"""
    session.pop("user_id", None)
    return redirect(url_for("home.login"))


@home_bp.route("/search/")
def search():
    """
    搜索景区
    """
    area = Area.query.all()
    area_id = request.args.get('area_id', type=int)
    star = request.args.get('star', type=int)
    if area_id or star:                                                 # 根据星级搜索景区
        filters = and_(Scenic.area_id == area_id, Scenic.star == star)
        all_scenic = Scenic.query.filter(filters)
    else:
        all_scenic = Scenic.query.filter()
    count = all_scenic.count()
    return render_template("home/search.html",
                           area=area, area_id=area_id, star=star,
                           all_scenic=all_scenic, count=count)


@home_bp.route('/info/<int:id>')
def info(id=None):
    """
    景区详情页面 id为景区id
    """
    scenic = Scenic.query.get_or_404(int(id))
    user_id = session.get('user_id', None)
    if user_id:
        count = Collect.query.filter_by(user_id=int(user_id), scenic_id=int(id)).count()
    else:
        user_id = 0
        count = 0
    return render_template('home/info.html', scenic=scenic, user_id=user_id, count=count)


@home_bp.route("/travels/<int:id>")
def travels(id=None):
    """游记详细页面"""
    our_travels = Travels.query.get_or_404(int(id))
    return render_template("home/travels.html", travels=our_travels)


@home_bp.route("/collect_add/")
@user_login
def collect_add():
    """
       收藏景区
    """
    scenic_id = request.args.get("scenic_id")   # 接收传递的参数scenic_id
    print(scenic_id)
    user_id = session['user_id']                    # 获取当前用户的ID
    count = Collect.query.filter_by(        # 根据用户ID和景区ID判断是否该收藏
        user_id=int(user_id),
        scenic_id=int(scenic_id)
    ).count()
    # 已收藏
    if count:
        data1 = dict(ok=0)
    # 未收藏进行收藏
    else:
        collect = Collect(
            user_id=int(user_id),
            scenic_id=int(scenic_id)
        )
        db.session.add(collect)                       # 添加数据
        db.session.commit()                           # 提交数据
        data1 = dict(ok=1)                             # 写入字典
    import json                                       # 导入模块
    return json.dumps(data1)                           # 返回json数据


@home_bp.route("/collect_list/")
@user_login
def collect_list():
    """查看收藏景区列表"""
    collect_my = Collect.query.filter_by(user_id=session['user_id']).order_by(Collect.addtime.desc())
    count = collect_my.count()
    return render_template('home/collect_list.html', collect_my=collect_my, count=count)


@home_bp.route("/collect_cancel/")
@user_login
def collect_cancel():
    """
    取消收藏景区
    """
    scenic_id = request.args.get("scenic_id")                                      # 获取景区ID
    user_id = session["user_id"]                                                   # 获取当前用户ID
    print(scenic_id, user_id)
    collect = Collect.query.filter_by(scenic_id=scenic_id, user_id=user_id).first()  # 查找Collect表，查看记录是否存在
    if collect:                                                      # 如果存在
        db.session.delete(collect)                                    # 删除数据
        db.session.commit()                                           # 提交数据
        data = dict(ok=1)                                             # 写入字典
    else:
        data = dict(ok=0)                                             # 写入字典
    import json                                                       # 引入json模块
    return json.dumps(data)                                           # 输出json格式


@home_bp.route("/about/")
def about():
    """
    关于我们
    """
    return render_template('home/about.html')


@home_bp.route("/contact/", methods=['GET', 'POST'])
def contact():
    """联系我们"""
    form = SuggetionForm()
    if form.validate_on_submit():
        data = form.data
        suggestion = Suggestion(
            name=data["name"],                                # 昵称
            email=data["email"],                              # 联系邮件
            content=data["content"],                          # 内容
        )
        db.session.add(suggestion)
        db.session.commit()
        flash("已发送建议！", "ok")
    return render_template("home/contact.html", form=form)
