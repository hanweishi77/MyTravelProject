from flask_wtf import FlaskForm
import wtforms
from wtforms.validators import Email, length, EqualTo, DataRequired
from models import User


class RegisterForm(FlaskForm):
    """用户注册表单"""
    username = wtforms.StringField(
        "用户名", validators=[DataRequired("用户名不能为空"),
                           length(min=1, max=20, message="用户名长度不符")]
    )
    email = wtforms.StringField(
        "邮箱", validators=[DataRequired("邮箱不能为空"), Email("邮箱格式错误")]
    )
    pwd = wtforms.PasswordField(
        "密码", validators=[DataRequired(), length(min=6, max=20, message="密码格式错误")]
    )
    re_pwd = wtforms.PasswordField(
        "确认密码", validators=[DataRequired("请确认密码"), EqualTo("pwd", message="两次密码不一致")]
    )
    submit = wtforms.SubmitField("注册")

    def validate_email(self, field):
        email = field.data
        user = User.query.filter_by(email=email).first()
        if user:
            raise wtforms.ValidationError(message="该邮箱已经被注册！")

    # 自定义验证 1.邮箱是否被注册  2.验证码是否正确
    """
    

    def validate_vaptcha(self, field):
        captcha = field.captcha
        email = self.my_email.data
        captcha_model = EmailCaptchaModel.filter_by(email=email, captcha=captcha.first())
        if not captcha_model:
            raise wtforms.ValidationError(message="邮箱或验证码错误！")
        else:
            db.session.delete(captcha_model)
            db.session.commit()
    """


class LoginForm(FlaskForm):
    """
    登录功能
    """
    email = wtforms.StringField(
        validators=[
            DataRequired("邮箱不能为空！")
        ],
        description="邮箱",
        render_kw={
            "type": "email",
            "placeholder": "请输入邮箱！",
        }
    )
    pwd = wtforms.PasswordField(
        validators=[
            DataRequired("密码不能为空！")
        ],
        description="密码",
        render_kw={
            "type": "password",
            "placeholder": "请输入密码！",
        }
    )
    submit = wtforms.SubmitField(
        '登录',
    )


class SuggetionForm(FlaskForm):
    """意见建议"""
    name = wtforms.StringField(
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
    email = wtforms.StringField(
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
    content = wtforms.TextAreaField(
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
    submit = wtforms.SubmitField(
        '发送消息',
        render_kw={
            "class": "btn-submit"
        }
    )
