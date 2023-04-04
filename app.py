# _*_ codding:utf-8 _*_
from flask import Flask
import config
from extendsions import db
from flask_migrate import Migrate
from blueprints.home import home_bp
from blueprints.admin import admin_bp
from flask_ckeditor import CKEditor


"""Flask类构造程序实例app,绑定到当前模块"""
app = Flask(__name__)
app.config.from_object(config)                          # 配置

"""数据库绑定，以及一些控制设置"""
db.init_app(app)

"""创建富文本编辑器对象ckeditor"""
ckeditor = CKEditor(app)

"""创建迁移数据库的操作对象migrate"""
migrate = Migrate(app, db)

"""注册项目蓝图"""
app.register_blueprint(home_bp)
app.register_blueprint(admin_bp)


if __name__ == "__main__":
    app.run()
