# _*_ codding:utf-8 _*_
from flask import Flask
import config
from extendsions import db, mail
from flask_migrate import Migrate
from blueprints.home import home_bp
from blueprints.admin import admin_bp
from flask_ckeditor import CKEditor


# Flask类构造程序实例app,绑定到当前模块
app = Flask(__name__)
app.config.from_object(config)                          # 配置加载

# 数据库操作对象db初始化，以及一些控制设置
db.init_app(app)

# 富文本编辑器对象ckeditor，会生成一个蓝图
ckeditor = CKEditor(app)

# 邮箱服务器对象mail初始化，以及一些控制设置
mail.init_app(app)

# 迁移数据库的操作对象migrate
migrate = Migrate(app, db)

# 注册项目蓝图
app.register_blueprint(home_bp)
app.register_blueprint(admin_bp)


if __name__ == "__main__":
    app.run()
