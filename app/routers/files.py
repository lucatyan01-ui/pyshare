# from fastapi import APIRouter  # 导入 APIRouter，用来创建文件管理相关路由
from fastapi import APIRouter, Request  # 导入 APIRouter 和 Request，Request 用来把请求信息传给模板
from fastapi.templating import Jinja2Templates  # 导入 Jinja2Templates，用来返回 HTML 模板页面


router = APIRouter()  # 创建文件管理路由对象，后面的 /files 页面会挂到这个 router 上


templates = Jinja2Templates(directory="app/templates")  # 指定 HTML 模板文件所在目录


@router.get("/files")  # 注册一个 GET 接口，访问地址是 /files
def files_page(request: Request):  # 定义文件管理页面处理函数，并接收浏览器请求对象
    return templates.TemplateResponse(  # 返回 HTML 模板响应
        "files.html",  # 指定要渲染的模板文件名
        {"request": request},  # 把 request 传给模板，这是 FastAPI 模板要求的
    )
