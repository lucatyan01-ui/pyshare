from fastapi import FastAPI  # 从 fastapi 库中导入 FastAPI 类，用它创建 Web 应用

from app.core.config import settings  # 导入项目配置对象，读取项目名、调试开关等配置


app = FastAPI(  # 创建一个 FastAPI 应用对象，并把它保存到变量 app 里
    title=settings.app_name,  # 从配置中读取项目名称，显示在接口文档页面
    debug=settings.debug,  # 从配置中读取是否开启调试模式
)


@app.get("/health")  # 注册一个 GET 接口，访问地址是 /health
def health_check():  # 定义接口处理函数，访问 /health 时会执行这个函数
    return {"status": "ok"}  # 返回一个字典，FastAPI 会自动转换成 JSON 响应
