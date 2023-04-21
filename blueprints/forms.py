from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import Email, length, EqualTo, DataRequired
from models import User, EmailCaptcha
from extendsions import db


class RegisterForm(FlaskForm):
    """
    用户注册表单
    """
    email = StringField(
        "邮箱", validators=[DataRequired("邮箱不能为空！"), Email("邮箱格式错误！")]
    )
    captcha = StringField(
        label="验证码",
        validators=[DataRequired("验证码不能为空！"), length(min=4, max=4, message="验证码长度错误！")],
        render_kw={
            "id": "captcha",
        }
    )
    username = StringField(
        "用户名", validators=[DataRequired("用户名不能为空！"),
                           length(min=1, max=12, message="用户名长度不符！")]
    )
    pwd = PasswordField(
        "密码", validators=[DataRequired("密码不能为空！"), length(min=6, max=20, message="密码格式错误！")]
    )
    re_pwd = PasswordField(
        "确认密码", validators=[DataRequired("请确认密码!"), EqualTo("pwd", message="密码不一致！")]
    )
    submit = SubmitField("注册")

    def validate(self, extra_validators=None):
        initial_validation = super(RegisterForm, self).validate()
        if not initial_validation:
            return False
        user = User.query.filter_by(email=self.email.data).first()
        captcha = EmailCaptcha.query.filter_by(captcha=self.captcha.data, email=self.email.data).first()
        if user:
            self.email.errors.append("邮箱已存在！")
            return False
        if not captcha:
            self.captcha.errors.append("验证码错误！")
            return False
        return True


class LoginForm(FlaskForm):
    """
    登录功能
    """
    email = StringField(
        validators=[
            DataRequired("邮箱不能为空！")
        ],
        description="邮箱",
        render_kw={
            "type": "email",
            "placeholder": "请输入邮箱！",
        }
    )
    pwd = PasswordField(
        validators=[
            DataRequired("密码不能为空！")
        ],
        description="密码",
        render_kw={
            "type": "password",
            "placeholder": "请输入密码！",
        }
    )

    submit = SubmitField(
        '登录',
    )

    def validate(self, extra_validators=None):
        initial_validation = super(LoginForm, self).validate()
        if not initial_validation:
            return False
        user = User.query.filter_by(email=self.email.data).count()
        if user == 0:
            self.email.errors.append("邮箱不存在")
            return False
        return True


class SuggetionForm(FlaskForm):
    """意见建议"""
    name = StringField(
        label="姓名",
        validators=[
            DataRequired("姓名不能为空！"), length(min=1, max=20, message="用户名长度不符")
        ],
        description="姓名",
        render_kw={
            "placeholder": "请输入姓名！",
            "class": "form-control"
        }
    )
    email = StringField(
        label="邮箱",
        validators=[
            DataRequired("邮箱不能为空！"), Email("邮箱格式错误")
        ],
        description="邮箱",
        render_kw={
            "placeholder": "请输入邮箱！",
            "class": "form-control"
        }
    )
    content = TextAreaField(
        label="意见建议",
        validators=[
            DataRequired("内容不能为空！")
        ],
        description="意见建议",
        render_kw={
            "placeholder": "请输入内容！",
            "class": "form-control",
            "row": 10
        }
    )
    submit = SubmitField(
        '发送消息',
        render_kw={
            "class": "btn-submit"
        }
    )

    def validate(self, extra_validators=None):
        initial_validation = super(SuggetionForm, self).validate()
        if not initial_validation:
            return False
        return True
