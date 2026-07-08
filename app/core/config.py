from functools import lru_cache  # 导入缓存工具，避免重复创建配置对象

from pydantic_settings import BaseSettings, SettingsConfigDict  # 导入读取环境变量的配置基类


class Settings(BaseSettings):  # 定义项目的统一配置类
    app_name: str = "pyshare"  # 项目名称，默认是 pyshare
    app_env: str = "development"  # 当前运行环境，默认是开发环境
    debug: bool = True  # 是否开启调试模式，开发时通常为 true

    host: str = "127.0.0.1"  # 本地服务监听地址
    port: int = 8000  # 本地服务监听端口

    database_url: str = "sqlite:///./pyshare.sqlite3"  # 数据库连接地址，默认使用 SQLite

    secret_key: str = "change-me"  # 项目密钥，正式环境必须改成安全随机值
    access_token_expire_minutes: int = 60  # 登录令牌有效时间，单位是分钟

    upload_dir: str = "uploads"  # 上传文件保存目录
    max_upload_size_mb: int = 100  # 单个上传文件的最大体积，单位是 MB

    model_config = SettingsConfigDict(  # 配置 pydantic-settings 如何读取环境变量
        env_file=".env",  # 指定从项目根目录的 .env 文件读取配置
        env_file_encoding="utf-8",  # 指定 .env 文件编码为 UTF-8
        extra="ignore",  # 如果 .env 里有暂时不用的变量，就忽略它们
    )


@lru_cache  # 缓存函数结果，让 settings 对象只创建一次
def get_settings() -> Settings:  # 定义一个获取配置对象的函数
    return Settings()  # 创建并返回 Settings 配置对象


settings = get_settings()  # 创建全局配置对象，其他文件可以直接导入使用
