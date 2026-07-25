from fastapi import APIRouter  # 导入 APIRouter，用来创建一组路由


router = APIRouter()  # 创建一个路由对象，后面的接口先挂到这个 router 上


@router.get("/health")  # 注册一个 GET 接口，访问地址是 /health
def health_check():  # 定义接口处理函数，访问 /health 时会执行这个函数
    return {"status": "ok"}  # 返回一个字典，FastAPI 会自动转换成 JSON 响应
