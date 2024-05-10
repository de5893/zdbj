从烧瓶导入烧瓶
从flask_sqlalchemy导入SQLAlchemy
导入pymysql
导入配置

# 因MySQLDB不支持Python3，使用pymysql扩展库代替MySQLDB库
pymysql。install_as_MySQLdb  (   ）

db = SQLAlchemy    (    )      # 初始化DB操作对象，不绑定app

def     create_app    (    )：
    # 初始化web应用
    应用程序= Flask （ __name__，instance_relative_config = True）
    应用程序。配置[   '调试'  ] =配置。调试

    # 设置数据库链接
    应用程序。config [  'SQLALCHEMY_DATABASE_URI'   ] = 'mysql://{}:{}@{}/flask_demo'。格式（配置.用户名，配置.密码，
                                                                                 配置。数据库地址）
    D b。init_app    ( app )      # 绑定app到db

    # 加载控制器
    从wxcloudrun导入视图
    ideas。init_app    ( app )      # 将View函数的注册移到views.py中的一个函数

    # 加载配置
    应用程序。配置。from_object   (  '配置' )

    返回应用程序
