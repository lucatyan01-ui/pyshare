from pathlib import Path  # 导入 Path，用来处理文件和目录路径

# from fastapi import APIRouter  # 导入 APIRouter，用来创建文件管理相关路由
from fastapi import APIRouter, File, Request, UploadFile  # 导入路由、文件上传和请求相关工具
from fastapi.responses import FileResponse, RedirectResponse  # 导入文件下载响应和重定向响应
from fastapi.templating import Jinja2Templates  # 导入 Jinja2Templates，用来返回 HTML 模板页面


router = APIRouter()  # 创建文件管理路由对象，后面的 /files 页面会挂到这个 router 上


templates = Jinja2Templates(directory="app/templates")  # 指定 HTML 模板文件所在目录


upload_dir = Path("uploads")  # 指定上传文件保存目录
upload_dir.mkdir(exist_ok=True)  # 如果 uploads 目录不存在，就自动创建


def get_upload_file_path(filename: str):  # 根据文件名生成安全的上传文件路径
    file_path = upload_dir / filename  # 先拼出文件路径
    resolved_upload_dir = upload_dir.resolve()  # 获取 uploads 目录的绝对路径
    resolved_file_path = file_path.resolve()  # 获取目标文件的绝对路径

    if resolved_upload_dir not in resolved_file_path.parents:  # 判断目标文件是否在 uploads 目录里面
        return None  # 如果不在 uploads 目录里，返回 None，表示非法路径

    return file_path  # 路径合法时，返回文件路径


@router.get("/files")  # 注册一个 GET 接口，访问地址是 /files
def files_page(request: Request):  # 定义文件管理页面处理函数，并接收浏览器请求对象
    files = [path.name for path in upload_dir.iterdir() if path.is_file()]  # 读取 uploads 目录中的文件名列表
    return templates.TemplateResponse(  # 返回 HTML 模板响应
        "files.html",  # 指定要渲染的模板文件名
        {"request": request, "files": files},  # 把 request 和文件列表传给模板
    )


@router.get("/files/download/{filename}")  # 注册一个 GET 接口，用来下载指定文件
def download_file(filename: str):  # filename 来自网址中的 {filename}，类型是字符串
    file_path = get_upload_file_path(filename)  # 根据文件名生成安全的文件路径

    if file_path is None or not file_path.is_file():  # 如果路径非法，或者文件不存在
        return RedirectResponse(url="/files", status_code=303)  # 回到文件列表页面

    return FileResponse(path=file_path, filename=filename)  # 把服务器上的文件返回给浏览器下载


@router.post("/files/delete/{filename}")  # 注册一个 POST 接口，用来删除指定文件
def delete_file(filename: str):  # filename 来自网址中的 {filename}，类型是字符串
    file_path = get_upload_file_path(filename)  # 根据文件名生成安全的文件路径

    if file_path is None:  # 如果路径非法
        return RedirectResponse(url="/files", status_code=303)  # 回到文件列表页面

    if file_path.is_file():  # 判断这个路径确实是一个文件
        file_path.unlink()  # 删除这个文件
    return RedirectResponse(url="/files", status_code=303)  # 删除完成后重定向回文件列表页面


@router.post("/files/upload")  # 注册一个 POST 接口，接收文件上传表单
def upload_file(upload_file: UploadFile = File(...)):  # 接收表单中 name="upload_file" 的文件
    file_path = get_upload_file_path(upload_file.filename)  # 根据上传文件名生成安全的文件路径

    if file_path is None:  # 如果上传文件名不安全
        return RedirectResponse(url="/files", status_code=303)  # 回到文件列表页面

    content = upload_file.file.read()  # 读取上传文件的全部内容
    file_path.write_bytes(content)  # 把文件内容写入服务器本地磁盘
    # 旧写法：上传成功后返回 JSON 数据，浏览器页面会停在 JSON 结果页。
    # return {"filename": upload_file.filename, "saved_to": str(file_path)}  # 返回保存结果
    return RedirectResponse(url="/files", status_code=303)  # 上传成功后重定向回文件列表页面
