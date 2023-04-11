from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import Email, length, EqualTo, DataRequired
from models import User


class RegisterForm(FlaskForm):
    """用户注册表单"""
    username = StringField(
        "用户名", validators=[DataRequired("用户名不能为空"),
                           length(min=1, max=20, message="用户名长度不符")]
    )
    email = StringField(
        "邮箱", validators=[DataRequired("邮箱不能为空"), Email("邮箱格式错误")]
    )
    pwd = PasswordField(
        "密码", validators=[DataRequired(), length(min=6, max=20, message="密码格式错误")]
    )
    re_pwd = PasswordField(
        "确认密码", validators=[DataRequired("请确认密码"), EqualTo("pwd", message="两次密码不一致")]
    )
    submit = SubmitField("注册")

    def validate(self, extra_validators=None):
        initial_validation = super(RegisterForm, self).validate()
        if not initial_validation:
            return False
        user = User.query.filter_by(email=self.email.data).first()
        if user:
            self.email.errors.append("邮箱已存在")
            return False
        if self.pwd.data != self.re_pwd.data:
            self.pwd.errors.append("密码不一致")
            return False
        return True
    """
    def validate_email(self, field, extra_validators=None):
        email = field.data
        user = User.query.filter_by(email=email).first()
        if user:
            raise wtforms.ValidationError(message="该邮箱已经被注册！")
    """
    # 自定义验证 1.邮箱是否被注册  2.验证码是否正确


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
