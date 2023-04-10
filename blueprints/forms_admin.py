from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import StringField, PasswordField, SubmitField, SelectField, \
    FileField, TextAreaField, RadioField
from wtforms.validators import DataRequired, ValidationError, EqualTo
from models import Admin
from flask import session
from flask_ckeditor.fields import CKEditorField


class LoginForm(FlaskForm):
    """
    管理员登录表单
    """
    name = StringField(
        label="账号",
        validators=[
            DataRequired("账号不能为空")
        ],
        description="账号",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入账号！",
        }
    )
    pwd = PasswordField(
        label="密码",
        validators=[
            DataRequired("密码不能为空")
        ],
        description="密码",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入密码！",
        }
    )
    submit = SubmitField(
        '登录',
        render_kw={
            "class": "btn btn-primary btn-block btn-flat",
        }
    )

    def validate(self, extra_validators=None):
        initial_validation = super(LoginForm, self).validate()
        if not initial_validation:
            return False
        admin = Admin.query.filter_by(name=self.name.data).count()
        if admin == 0:
            self.name.errors.append("账号不存在")
            return False
        return True
    # 验证账号，命名规则：validate_ + 字段名。如果要验证密码，则可以创建函数validate_pwd
    """
    def validate_name(self, field):
        name = field.data
        admin = Admin.query.filter_by(name=name).count()
        if admin == 0:
            raise ValidationError("账号不存在! ")
    """


class PwdForm(FlaskForm):
    """
    修改密码表表单
    """
    old_pwd = PasswordField(
        label="旧密码",
        validators=[
            DataRequired("旧密码不能为空！")
        ],
        description="旧密码",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入旧密码！",
        }
    )
    new_pwd = PasswordField(
        label="新密码",
        validators=[
            DataRequired("新密码不能为空！")
        ],
        description="新密码",
        render_kw={
            "class": "form-control",
            "placeholder": "新密码！",
        }
    )
    re_pwd = PasswordField(
        label="确认密码",
        validators=[DataRequired("确认密码"), EqualTo("new_pwd", message="两次密码不一致")],
        render_kw={
            "class": "form-control",
            "placeholder": "确认新密码",
        }
    )
    submit = SubmitField(
        label='保存',
        render_kw={
            "class": "btn btn-primary btn-block",
        }
    )

    def validate(self, extra_validators=None):
        initial_validation = super(PwdForm, self).validate()
        if not initial_validation:
            return False
        name = session["admin"]
        admin = Admin.query.filter_by(name=name).first()
        if not admin.check_pwd(self.old_pwd.data):
            self.old_pwd.errors.append("旧密码错误")
            return False
        return True

    """
    def validate_old_pwd(self, field):
        old_pwd = field.data
        name = session["admin"]
        admin = Admin.query.filter_by(
            name=name
        ).first()
        if not admin.check_pwd(old_pwd):
            raise ValidationError("旧密码错误！")
    """


class ScenicForm(FlaskForm):
    """
    景区表表单
    """
    # id = db.Column(db.Integer, primary_key=True)  # 编号
    # title = db.Column(db.String(200))  # 标题
    title = StringField(
        label="景区名称",
        validators=[DataRequired("名称不能为空！")],
        render_kw={
            "class": "form-control",
            "placeholder": "请输入景区名称！",
        }
    )
    # star = db.Column(db.Integer)  # 星级
    star = SelectField(
        label="星级",
        validators=[
            DataRequired("请选择星级！")
        ],
        coerce=int,                                                                    # 强制数据类型转换
        choices=[(1, "1星"), (2, "2星"), (3, "3星"), (4, "4星"), (5, "5星")], default=5,
        description="星级",
        render_kw={
            "class": "form-control",
        }
    )
    # logo = db.Column(db.String(200), unique=True)  # 景区图片名，图片存本地
    logo = FileField(
        label="封面图片",
        validators=[
            DataRequired("请上传封面！"),
            FileAllowed(['jpg', 'jpeg', 'png'], '请上传jpg或png格式图片!')
        ],
        description="封面图片",
    )
    # introduction = db.Column(db.Text)  # 景区介绍文本
    introduction = TextAreaField(
        label="景区简介",
        validators=[
            DataRequired("简介不能为空！")
        ],
        description="简介",
        render_kw={
            "class": "form-control",
            "rows": 2
        }
    )
    # content = db.Column(db.Text)  # 景区内容描述
    content = CKEditorField(
        label="景区内容",
        validators=[
            DataRequired("内容不能为空！")
        ],
        render_kw={
            "class": "form-control ckeditor",
            "rows": 10
        }
    )
    # address = db.Column(db.Text)  # 景区地址
    address = StringField(
        label="地址",
        validators=[DataRequired("地址不能为空！")],
        render_kw={
            "class": "form-control",
            "placeholder": "请输入景区地址！"
        }
    )
    # is_hot = db.Column(db.Boolean(), default=0)  # 是否热门
    is_hot = RadioField(
        label='是否热门',
        coerce=int,
        choices=[(0, '否'), (1, '是')], default=0,
    )
    # is_recommended = db.Column(db.Boolean(), default=0)  # 是否推荐
    is_recommended = RadioField(
        label='是否推荐',
        coerce=int,
        choices=[(0, '否'), (1, '是')], default=0,
    )
    # area_id = db.Column(db.Integer, db.ForeignKey("area.id"))  # 关联外键，所属地区id
    area_id = SelectField(
        label="所属地区",
        validators=[
            DataRequired("请选择标签！")
        ],
        coerce=int,
        description="所属地区",
        render_kw={
            "class": "form-control",
        },
    )
    submit = SubmitField(
        label='添加',
        render_kw={
            "class": "btn btn-primary",
        }
    )


class AreaForm(FlaskForm):
    """
    地区表表单
    """
    # 数据库数据模型对照
    # id = db.Column(db.Integer, primary_key=True)                           # 编号
    # name = db.Column(db.String(70), unique=True)                           # 标题
    name = StringField(
        label="地区名称",
        validators=[DataRequired("地区名不能为空！")],
        render_kw={
            "class": "form-control",
            "placeholder": "请输入地区名称！",
        }
    )
    # addtime = db.Column(db.DateTime, index=True, default=datetime.now)     # 添加景区时间,添加索引
    # is_recommended = db.Column(db.Boolean(), default=0)                    # 景区推荐
    is_recommended = RadioField(
        label='是否推荐',
        coerce=int,
        choices=[(0, '否'), (1, '是')], default=0,
    )
    # introduction = db.Column(db.Text)                                      # 景区介绍
    introduction = TextAreaField(
        label="地区简介",
        validators=[
            DataRequired("简介不能为空！")
        ],
        description="简介",
        render_kw={
            "class": "form-control",
            "rows": 5
        }
    )
    submit = SubmitField(
        label='添加',
        render_kw={
            "class": "btn btn-primary",
        }
    )


class TravelsForm(FlaskForm):
    """
    游记表表单
    """
    # 游记表数据库模型对照
    # title = db.Column(db.String(200), unique=True)
    title = StringField(
        label="标题",
        validators=[DataRequired("标题不能为空！")],
        render_kw={
            "class": "form-control",
            "placeholder": "游记标题",
        }
    )
    # author = db.Column(db.String(70))                                    # 作者
    author = StringField(
        label="作者",
        validators=[DataRequired("请输入作者名！")],
        render_kw={
            "class": "form-control",
            "placeholder": "作者名",
        }
    )
    # content = db.Column(db.Text)
    content = CKEditorField(
        label="游记内容",
        validators=[
            DataRequired("内容不能为空！")
        ],
        description="游记内容",
        render_kw={
            "class": "form-control",
            "rows": 8,
        }
    )
    # scenic_id = db.Column(db.Integer, db.ForeignKey("scenic.id"))
    scenic_id = SelectField(
        label="所属景区",
        validators=[
            DataRequired("景区")
        ],
        coerce=int,                                                          # 强制数据类型转换
        description="所属景区",
        render_kw={
            "class": "form-control",
        }
    )
    submit = SubmitField(
        label='添加',
        render_kw={
            "class": "btn btn-primary",
        }
    )
