from pathlib import Path  # 导入 Path，用来处理文件和目录路径

# from fastapi import APIRouter  # 导入 APIRouter，用来创建文件管理相关路由
from fastapi import APIRouter, File, Request, UploadFile  # 导入路由、文件上传和请求相关工具
from fastapi.templating import Jinja2Templates  # 导入 Jinja2Templates，用来返回 HTML 模板页面


router = APIRouter()  # 创建文件管理路由对象，后面的 /files 页面会挂到这个 router 上


templates = Jinja2Templates(directory="app/templates")  # 指定 HTML 模板文件所在目录


upload_dir = Path("uploads")  # 指定上传文件保存目录


@router.get("/files")  # 注册一个 GET 接口，访问地址是 /files
def files_page(request: Request):  # 定义文件管理页面处理函数，并接收浏览器请求对象
    files = [path.name for path in upload_dir.iterdir() if path.is_file()]  # 读取 uploads 目录中的文件名列表
    return templates.TemplateResponse(  # 返回 HTML 模板响应
        "files.html",  # 指定要渲染的模板文件名
        {"request": request, "files": files},  # 把 request 和文件列表传给模板
    )


@router.post("/files/upload")  # 注册一个 POST 接口，接收文件上传表单
def upload_file(upload_file: UploadFile = File(...)):  # 接收表单中 name="upload_file" 的文件
    file_path = upload_dir / upload_file.filename  # 拼出文件保存路径，例如 uploads/a.txt
    content = upload_file.file.read()  # 读取上传文件的全部内容
    file_path.write_bytes(content)  # 把文件内容写入服务器本地磁盘
    return {"filename": upload_file.filename, "saved_to": str(file_path)}  # 返回保存结果
