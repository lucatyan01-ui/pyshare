from fastapi import APIRouter  # 导入 APIRouter，用来创建文件管理相关路由


router = APIRouter()  # 创建文件管理路由对象，后面的 /files 页面会挂到这个 router 上


@router.get("/files")  # 注册一个 GET 接口，访问地址是 /files
def files_page():  # 定义文件管理页面处理函数，访问 /files 时会执行它
    return {"title": "文件管理页面"}  # 先返回一个简单 JSON，证明 /files 页面能访问
