from extendsions import db
from datetime import datetime


# 会员表
class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)     # 编号，自增
    username = db.Column(db.String(70), nullable=False)                      # 用户名
    email = db.Column(db.String(50), nullable=False, unique=True)        # 邮箱
    pwd = db.Column(db.String(300), nullable=False)                      # 密码
    phone = db.Column(db.String(11), unique=True)                        # 手机号
    info = db.Column(db.Text)                                            # 个性简介
    face = db.Column(db.String(255), unique=True)                        # 头像
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)   # 注册时间
    collect = db.relationship('Collect', backref='user')                 # 收藏外键关系关联
    userlog = db.relationship("UserLog", backref="user")                 # 用户登录日志外键关系关联

    def check_pwd(self, pwd):
        """
        检测密码是否正确
        :param pwd: 密码
        :return: 返回布尔值
        """
        from werkzeug.security import check_password_hash
        return check_password_hash(self.pwd, pwd)


# 邮箱验证码存储
class EmailCaptcha(db.Model):
    __tablename__ = "emailcaptcha"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)                     # 编号，主键自增
    email = db.Column(db.String(50), nullable=False)                                     # 邮箱,非空
    captcha = db.Column(db.String(10), nullable=False)                                   # 验证码,非空
    tag = db.Column(db.Boolean, default=False)                                           # 标识


# 管理员表
class Admin(db.Model):
    __tablename__ = "admin"
    id = db.Column(db.Integer, primary_key=True)                  # 编号
    name = db.Column(db.String(100), unique=True)                 # 管理员账号
    pwd = db.Column(db.String(300))                               # 管理员密码
    adminlogs = db.relationship("Adminlog", backref='admin')      # 管理员登录日志外键关系关联
    oplogs = db.relationship("Oplog", backref='admin')            # 管理员操作日志外键关系关联

    def check_pwd(self, pwd):
        """
        检测加密的密码是否正确
        :param pwd: 密码
        :return: 返回布尔值
        """
        from werkzeug.security import check_password_hash
        return check_password_hash(self.pwd, pwd)


# 管理员登录日志表
class Adminlog(db.Model):
    __tablename__ = "adminlog"
    id = db.Column(db.Integer, primary_key=True)                         # 编号
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'))          # 所属管理员
    ip = db.Column(db.String(100))                                       # 登录IP
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)   # 登录时间
    
    
# 操作日志表
class Oplog(db.Model):
    __tablename__ = "oplog"
    id = db.Column(db.Integer, primary_key=True)                              # 编号
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'))               # 所属管理员
    ip = db.Column(db.String(100))                                            # 操作IP
    reason = db.Column(db.String(600))                                        # 操作原因
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)        # 登录时间


# 会员登录日志表
class UserLog(db.Model):
    __tablename__ = "userlog"
    id = db.Column(db.Integer, primary_key=True)                        # 编号
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))           # 设置外键 所属会员
    ip = db.Column(db.String(100))                                      # ip地址
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 登录时间


# 意见建议表
class Suggestion(db.Model):
    __tablename__ = "suggestion"
    id = db.Column(db.Integer, primary_key=True)                          # 编号
    name = db.Column(db.String(255))                                      # 昵称
    email = db.Column(db.String(100))                                     # 邮箱
    content = db.Column(db.Text)                                          # 意见内容
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)    # 注册时间


# 地区表
class Area(db.Model):
    __tablename__ = "area"
    id = db.Column(db.Integer, primary_key=True)                           # 编号
    name = db.Column(db.String(70), unique=True)                           # 标题
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)     # 添加景区时间,添加索引
    is_recommended = db.Column(db.Boolean(), default=0)                    # 景区推荐
    introduction = db.Column(db.Text)                                      # 景区介绍
    scenic = db.relationship("Scenic", backref="area")                     # 关联景区表


# 景区表
class Scenic(db.Model):
    __tablename__ = "scenic"
    id = db.Column(db.Integer, primary_key=True)                       # 编号
    title = db.Column(db.String(200))                                  # 标题
    star = db.Column(db.Integer)                                       # 星级
    logo = db.Column(db.String(200), unique=True)                      # 景区图片名，图片存本地
    introduction = db.Column(db.Text)                                  # 景区介绍文本
    content = db.Column(db.Text)                                       # 景区内容描述
    address = db.Column(db.Text)                                       # 景区地址
    is_hot = db.Column(db.Boolean(), default=0)                        # 是否热门
    is_recommended = db.Column(db.Boolean(), default=0)                # 是否推荐
    area_id = db.Column(db.Integer, db.ForeignKey("area.id"))          # 关联外键，所属地区id
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 添加时间
    collect = db.relationship("Collect", backref="scenic")             # 收藏表外键关联
    travels = db.relationship("Travels", backref="scenic")             # 游记表外键关联


# 收藏表
class Collect(db.Model):
    __tablename__ = "collect"
    id = db.Column(db.Integer, primary_key=True)                        # 编号
    scenic_id = db.Column(db.Integer, db.ForeignKey("scenic.id"))       # 所属景区
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))           # 所属用户
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 添加时间


# 游记表
class Travels(db.Model):
    __tablename__ = "travels"
    id = db.Column(db.Integer, primary_key=True)                         # 编号
    title = db.Column(db.String(200), unique=True)                       # 标题
    author = db.Column(db.String(70))                                    # 作者
    content = db.Column(db.Text)                                         # 游记内容
    scenic_id = db.Column(db.Integer, db.ForeignKey("scenic.id"))        # 所属景区id
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)   # 添加时间，作索引字段
