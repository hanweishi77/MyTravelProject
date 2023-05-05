import os

# 连接mysql数据库的配置
HOSTNAME = "127.0.0.1"                                    # 本机
PORT = 3306                                               # 端口
USERNAME = "root"                                         # 连接用户
PASSWORD = "123456"                                       # 用户密码
DATABASE = "my_travel_db"                                 # 数据库
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI                          # SQLALCHEMY_DATABASE_URI为系统变量名
SQLALCHEMY_TRACK_MODIFICATIONS = False                    # 设置是否跟踪数据库的修改情况，一般不跟踪
SQLALCHEMY_ECHO = True                                    # 数据库操作时后台显示原始SQL语句


# 通讯密钥，表单post提交需要
SECRET_KEY = "123456"


# 文件上传保存根路径
UP_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), "static/uploads/")


# Flask-CKEditor 配置
CKEDITOR_SERVE_LOCAL = True                               # 是否使用内置的本地资源，js文件来源
CKEDITOR_FILE_UPLOADER = 'admin.ckupload'                 # ckeditor文件上传


# 邮箱服务配置
MAIL_SERVER = "smtp.qq.com"                               # 邮箱服务器，这是QQ的
MAIL_USE_SSL = True                                       # 是否加密通讯
MAIL_PORT = 465                                           # 邮箱端口号
MAIL_USERNAME = "2276234553@qq.com"                       # 发送邮件所用的用户名，一般设置成邮箱账号就好
MAIL_PASSWORD = "你自己的邮箱授权码"                            # SMTP服务的授权码
MAIL_DEFAULT_SENDER = "2276234553@qq.com"                 # 默认发送者，邮箱账号即可

