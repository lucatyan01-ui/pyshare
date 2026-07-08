from collections.abc import Generator  # 导入 Generator 类型，用来标注 get_db 的返回类型

from sqlalchemy import create_engine  # 导入创建数据库引擎的函数
from sqlalchemy.orm import Session, sessionmaker  # 导入数据库会话类型和会话工厂

from app.core.config import settings  # 导入项目统一配置，里面包含数据库连接地址


connect_args = {}  # 创建数据库连接参数，默认先为空

if settings.database_url.startswith("sqlite"):  # 如果使用的是 SQLite 数据库
    connect_args["check_same_thread"] = False  # 允许 FastAPI 在不同线程中使用 SQLite 连接


engine = create_engine(  # 创建 SQLAlchemy 数据库引擎
    settings.database_url,  # 使用配置文件中的数据库连接地址
    connect_args=connect_args,  # 传入数据库连接参数
)


SessionLocal = sessionmaker(  # 创建数据库会话工厂，后面每次请求都从这里生成会话
    autocommit=False,  # 关闭自动提交，避免数据库操作在不明确时自动保存
    autoflush=False,  # 关闭自动刷新，由代码自己决定何时同步数据
    bind=engine,  # 把会话工厂绑定到上面创建的数据库引擎
)


def get_db() -> Generator[Session, None, None]:  # 定义 FastAPI 依赖函数，用来获取数据库会话
    db = SessionLocal()  # 创建一个新的数据库会话
    try:  # 开始使用数据库会话
        yield db  # 把数据库会话交给调用方使用
    finally:  # 不管接口执行成功还是失败，最后都会执行这里
        db.close()  # 关闭数据库会话，释放连接资源
