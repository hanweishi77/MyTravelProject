import os


HOSTNAME = "127.0.0.1"
PORT = 3306
USERNAME = "root"
PASSWORD = "123456"
DATABASE = "my_travel_db"

# 连接数据库的配置，SQLALCHEMY_DATABASE_URI为系统变量名
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False    # 设置是否跟踪数据库的修改情况，一般不跟踪
SQLALCHEMY_ECHO = True                    # 数据库操作时后台显示原始SQL语句，一般都是打开的，因为我们后台要日志
SECRET_KEY = "123456"                     # 数据库密钥


UP_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), "static/uploads/")      # 文件上传根路径


# Flask-CKEditor config
CKEDITOR_SERVE_LOCAL = True                        # 使用内置的本地资源
CKEDITOR_FILE_UPLOADER = 'admin.ckupload'          # ckeditor文件上传的url
