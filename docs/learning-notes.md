# Python 项目学习笔记

这份笔记记录学习 Python、Git、项目结构和后续容器知识时的重要概念。项目只是练习场，主要目标是学会编程和工程化思维。

## 1. 当前项目是什么

项目名称：`pyshare`

项目目标：做一个基于 FastAPI 的文件分享项目。

学习目标：

- 学 Python 基础语法
- 学 Git 版本管理
- 学项目目录结构
- 学后端接口开发
- 学数据库
- 学容器和部署

## 2. 常见项目文件

### README.md

项目说明文档。

通常写：

- 项目是干什么的
- 怎么安装依赖
- 怎么运行项目
- 项目目录结构

### .gitignore

Git 忽略规则文件。

作用：告诉 Git 哪些文件不要提交。

常见忽略项：

```gitignore
.DS_Store
__pycache__/
*.pyc
.env
.venv/
```

### .env.example

环境变量示例文件。

作用：告诉开发者项目需要哪些配置，但不放真实密码。

真实运行时通常复制一份：

```bash
cp .env.example .env
```

### requirements.txt

Python 依赖清单。

安装依赖时使用：

```bash
pip install -r requirements.txt
```

### __init__.py

Python 包标记文件。

有了它，目录可以被 Python 当作包导入。

例如：

```python
from app.core.config import settings
```

## 3. Git 基础

Git 用来管理代码版本。

### 三个区域

```text
工作区    正在编辑的文件
暂存区    准备提交的一批改动
本地仓库  已经保存好的版本记录
```

### 常用命令

查看当前状态：

```bash
git status
```

把当前目录所有改动加入暂存区：

```bash
git add .
```

提交成一个本地版本：

```bash
git commit -m "初始化项目结构"
```

查看提交历史：

```bash
git log --oneline
```

### 已完成的第一次提交

提交信息：

```text
f3ae8af 初始化项目结构
```

含义：

- `f3ae8af` 是提交编号
- `初始化项目结构` 是提交说明
- 这次提交保存了项目基础文件和目录

## 4. Python import

`import` 的作用：把别人写好的工具拿进来用。

格式一：

```python
import 模块名
```

格式二：

```python
from 模块名 import 工具名
```

例子：

```python
from datetime import datetime
```

意思是：从 `datetime` 模块里导入 `datetime` 这个类。

项目中的例子：

```python
from functools import lru_cache
```

意思是：从 Python 自带的 `functools` 模块里导入 `lru_cache`。

```python
from pydantic_settings import BaseSettings, SettingsConfigDict
```

意思是：从第三方库 `pydantic_settings` 里导入 `BaseSettings` 和 `SettingsConfigDict`。

## 5. Python class

`class` 用来定义类。

类可以先理解成“模板”。

项目中的例子：

```python
class Settings(BaseSettings):
```

意思是：定义一个叫 `Settings` 的配置类。

`BaseSettings` 是它继承的父类，让 `Settings` 拥有读取环境变量的能力。

## 6. 变量、类型标注和默认值

项目中的例子：

```python
debug: bool = True
```

拆开理解：

```text
debug  变量名
bool   类型，表示布尔值
True   默认值，表示真
```

通用格式：

```python
变量名: 类型 = 默认值
```

常见类型：

```text
str   字符串
int   整数
bool  布尔值，只有 True / False
```

更多例子：

```python
app_name: str = "pyshare"
port: int = 8000
debug: bool = True
```

## 7. app/core/config.py 的作用

`config.py` 是项目配置中心。

它负责把 `.env` 里的配置变成 Python 可以使用的对象。

例如 `.env.example` 中有：

```text
APP_NAME=pyshare
PORT=8000
```

代码中可以通过：

```python
settings.app_name
settings.port
```

来读取配置。

一句话记忆：

```text
config.py = 把配置文件变成 Python 变量
```

## 8. app/db/session.py 的作用

`session.py` 是数据库连接和会话管理文件。

它通常负责：

- 读取数据库地址
- 创建数据库引擎
- 创建数据库会话
- 在接口用完数据库后关闭连接

一句话记忆：

```text
session.py = 帮项目连接数据库，并在用完后关闭连接
```

## 9. 今日小练习

题目：

```python
from datetime import datetime
```

回答：

```text
从 datetime 库/模块导入 datetime。
```

题目：

```python
debug: bool = True
```

回答：

```text
debug 变量的类型是 bool，默认值是 True。
```

这个回答是正确的。

## 10. FastAPI 入口文件 app/main.py

今天创建了项目的第一个 Web 入口文件：

```text
app/main.py
```

当前完整代码：

```python
from fastapi import FastAPI  # 从 fastapi 库中导入 FastAPI 类，用它创建 Web 应用


app = FastAPI()  # 创建一个 FastAPI 应用对象，并把它保存到变量 app 里


@app.get("/health")  # 注册一个 GET 接口，访问地址是 /health
def health_check():  # 定义接口处理函数，访问 /health 时会执行这个函数
    return {"status": "ok"}  # 返回一个字典，FastAPI 会自动转换成 JSON 响应
```

### 这段代码做了什么

这段代码创建了一个 FastAPI Web 应用，并定义了第一个接口 `/health`。

当浏览器访问：

```text
http://127.0.0.1:8000/health
```

程序会执行：

```python
health_check()
```

然后返回：

```json
{"status": "ok"}
```

### 哪些是 Python 保留字

保留字是 Python 语言已经规定好用途的词，不能随便拿来当变量名。

这段代码里出现的保留字：

```text
from
import
def
return
```

含义：

- `from`：从某个模块里导入东西。
- `import`：导入某个工具、类、函数或模块。
- `def`：定义函数。
- `return`：返回函数结果。

### 哪些是库或框架提供的名字

这些不是我起的，是 FastAPI 框架提供的：

```text
fastapi
FastAPI
get
```

含义：

- `fastapi`：第三方库名称。
- `FastAPI`：FastAPI 库里的类，用来创建 Web 应用。
- `get`：FastAPI 应用对象的方法，用来注册 HTTP GET 接口。

### 哪些是我们自己起的名字

这些名字是我们自己定义的：

```text
app
health_check
/health
status
ok
```

含义：

- `app`：变量名，保存 FastAPI 应用对象。这个名字可以改，但大家通常都叫 `app`。
- `health_check`：函数名，表示健康检查。这个名字可以改，比如 `check_health`。
- `/health`：接口地址，是我们自己设计的 URL 路径。
- `status`：返回 JSON 里的字段名，是我们自己定的。
- `ok`：返回 JSON 里的字段值，是我们自己定的。

### 装饰器

这一行：

```python
@app.get("/health")
```

叫装饰器。

可以先理解成：把下面的函数注册成一个 Web 接口。

也就是说，这行代码把：

```python
health_check()
```

和访问地址：

```text
/health
```

绑定到一起。

### 容易出错的点

1. 括号必须是英文半角括号：

```python
FastAPI()
```

不能写成中文全角括号：

```python
FastAPI（）
```

2. `return` 后面建议加空格：

```python
return {"status": "ok"}
```

不要写成：

```python
return{"status": "ok"}
```

3. `return` 前面要缩进 4 个空格，因为它属于 `health_check` 函数内部。

## 11. 项目验证：运行 FastAPI 并访问 /health

今天第一次把项目真正运行起来，并在浏览器中验证了 `/health` 接口。

### 1. 创建虚拟环境

命令：

```bash
python3 -m venv .venv
```

含义：

```text
python3  使用 Python 3
-m venv  运行 Python 自带的 venv 模块
.venv    创建一个名叫 .venv 的虚拟环境目录
```

一句话理解：

```text
.venv = 当前项目自己的 Python 小环境
```

虚拟环境的作用：

- 不污染电脑全局 Python 环境。
- 不同项目可以安装不同版本的依赖。
- 让项目依赖更清楚、更容易迁移。

### 2. 查看隐藏目录

普通命令：

```bash
ls
```

不会显示以点开头的隐藏文件和目录。

所以 `.venv` 需要用：

```bash
ls -a
```

才能看到。

### 3. 启用虚拟环境

命令：

```bash
source .venv/bin/activate
```

启用成功后，终端前面会出现：

```text
(.venv)
```

这表示后面的 `python` 和 `pip` 默认都使用当前项目的虚拟环境。

### 4. pip 是什么

`pip` 是 Python 的软件包安装工具。

可以类比以前 Linux 里的 `yum`：

```text
yum  给 Linux 系统安装软件
pip  给 Python 项目安装 Python 库
```

例如：

```bash
pip install fastapi
```

表示安装 `fastapi` 这个 Python 库。

### 5. requirements.txt 是什么

`requirements.txt` 是 Python 项目的依赖清单。

里面记录项目需要安装哪些 Python 库和版本。

我们执行：

```bash
pip install -r requirements.txt
```

意思是：

```text
按照 requirements.txt 这个清单，批量安装项目依赖。
```

### 6. 启动 FastAPI 项目

命令：

```bash
uvicorn app.main:app --reload
```

拆开理解：

```text
uvicorn        启动 FastAPI 项目的服务器
app.main       找到 app/main.py 这个 Python 模块
app            找到 main.py 里的 app 变量
--reload       开发模式，代码变化后自动重启
```

启动成功时会看到：

```text
Uvicorn running on http://127.0.0.1:8000
```

### 7. 浏览器验证接口

访问：

```text
http://127.0.0.1:8000/health
```

看到：

```json
{"status":"ok"}
```

说明：

- FastAPI 项目启动成功。
- `app/main.py` 被正确加载。
- `/health` 接口能正常访问。
- 返回结果是正确的 JSON。

### 8. 终端日志怎么看

成功访问 `/health` 时，终端里看到：

```text
GET /health HTTP/1.1 200 OK
```

含义：

```text
GET      浏览器发起的是 GET 请求
/health 访问的是 /health 地址
200 OK   请求成功
```

### 9. favicon.ico 的 404

终端里还看到：

```text
GET /favicon.ico HTTP/1.1 404 Not Found
```

这个不是错误。

原因是：浏览器会自动请求网站小图标 `favicon.ico`。

我们现在还没有做网站图标，所以返回 `404 Not Found` 正常，不影响 `/health` 接口。

### 10. 停止服务

在 VS Code 终端里点击正在运行服务的终端区域，然后按：

```text
Control + C
```

看到类似：

```text
Application shutdown complete
```

说明服务已经停止。

## 12. Git 和 GitHub 的关系

今天把本地 `pyshare` 项目上传到了 GitHub。

### 1. 我的账号和仓库信息

GitHub 账号：

```text
lucatyan01-ui
```

Git 邮箱：

```text
lucatyan01@gmail.com
```

本地项目目录：

```text
/Users/lucatyan/work/python/pyshare
```

GitHub 远程仓库：

```text
https://github.com/lucatyan01-ui/pyshare.git
```

仓库状态：

```text
Private 私有仓库
```

项目说明：

```text
Python FastAPI file sharing project
```

### 2. Git 和 GitHub 分别是什么

一句话理解：

```text
Git    = 本地版本管理工具
GitHub = 网上保存、同步、展示 Git 仓库的平台
```

当前项目在本机有一个隐藏目录：

```text
.git
```

这个目录保存了本地 Git 仓库的提交历史。

GitHub 上的 `pyshare` 仓库是远程仓库，用来备份和同步代码。

### 3. local 和 remote

```text
local repository   本地仓库，在自己电脑上
remote repository  远程仓库，在 GitHub 上
```

本地仓库：

```text
/Users/lucatyan/work/python/pyshare
```

远程仓库：

```text
https://github.com/lucatyan01-ui/pyshare.git
```

### 4. origin 是什么

查看远程仓库：

```bash
git remote -v
```

当前输出：

```text
origin  https://github.com/lucatyan01-ui/pyshare.git (fetch)
origin  https://github.com/lucatyan01-ui/pyshare.git (push)
```

`origin` 是远程仓库地址的别名。

也就是说：

```text
origin = https://github.com/lucatyan01-ui/pyshare.git
```

`fetch` 表示可以从 GitHub 拉取代码。

`push` 表示可以把本地代码上传到 GitHub。

### 5. 添加远程仓库

今天执行过：

```bash
git remote add origin https://github.com/lucatyan01-ui/pyshare.git
```

含义：

```text
给当前本地仓库添加一个远程仓库地址，并把这个远程仓库命名为 origin。
```

### 6. 第一次 push

今天执行过：

```bash
git push -u origin main
```

拆开理解：

```text
git push  把本地提交上传到远程仓库
-u        建立本地 main 和远程 main 的默认关联
origin    远程仓库别名
main      当前主分支
```

成功时看到：

```text
branch 'main' set up to track 'origin/main'
```

意思是：

```text
本地 main 分支已经和 GitHub 上的 origin/main 分支建立关联。
```

以后本地提交后，可以直接执行：

```bash
git push
```

不用每次都写：

```bash
git push -u origin main
```

### 7. 平时提交和上传流程

以后每次改完代码，常用流程是：

```bash
git status
git add .
git commit -m "本次修改说明"
git push
```

含义：

```text
git status  查看哪些文件变了
git add .   把改动加入暂存区
git commit  保存成本地版本
git push    上传到 GitHub
```

### 8. 换电脑继续学习

第一次在新电脑下载项目：

```bash
git clone https://github.com/lucatyan01-ui/pyshare.git
cd pyshare
```

`clone` 的意思是：

```text
把 GitHub 上的远程仓库完整下载到本地，包括代码和提交历史。
```

以后在另一台电脑继续前，先拉取最新代码：

```bash
git pull
```

`pull` 的意思是：

```text
从 GitHub 拉取远程仓库的最新提交，合并到本地。
```

### 9. 下载别人的项目

如果别人的 GitHub 仓库是公开的，可以点击绿色 `Code` 按钮，复制 HTTPS 地址，然后执行：

```bash
git clone 别人的仓库地址
```

例如：

```bash
git clone https://github.com/someone/project.git
```

如果只是临时看代码，也可以点击：

```text
Code -> Download ZIP
```

但是 `Download ZIP` 只下载文件，不包含完整 Git 提交历史，所以不适合长期开发学习。

### 10. fork 是什么

`fork` 是 GitHub 上的复制操作。

可以理解成：

```text
把别人的仓库复制一份到自己的 GitHub 账号下。
```

常见场景：

- 想基于别人的项目做自己的版本。
- 想给开源项目贡献代码。
- 想先保存一份别人的项目。

### 11. 今天遇到的 GitHub 授权

第一次 `git push` 时，VS Code 弹出 GitHub 授权。

大致流程：

```text
VS Code 请求登录 GitHub
浏览器打开 GitHub 授权页面
选择 lucatyan01-ui 账号
授权 Visual Studio Code
邮箱验证码确认身份
回到 VS Code
重新 git push
```

遇到 Safari 显示无法连接 `127.0.0.1` 的回调页面时，不是项目错误。

原因是浏览器回调 VS Code 授权时没有接上。

处理方式：

```text
回到 VS Code，按提示重新授权，或者重新执行 git push。
```

最后 push 成功，说明本地仓库和 GitHub 已经连通。

### 12. GitHub 页面怎么看

仓库首页左上角：

```text
lucatyan01-ui / pyshare
```

表示：

```text
账号名 / 仓库名
```

`Private` 表示私有仓库。

文件列表里能看到：

```text
app
docs
.env.example
.gitignore
README.md
requirements.txt
```

说明本地文件已经上传到了 GitHub。

绿色 `Code` 按钮可以：

- 复制仓库地址。
- 使用 `git clone` 下载项目。
- 下载 ZIP 文件。

## 13. main.py 接入配置对象 settings

今天把 `app/main.py` 从简单写法：

```python
app = FastAPI()
```

升级成了读取配置的写法：

```python
app = FastAPI(  # 创建一个 FastAPI 应用对象，并把它保存到变量 app 里
    title=settings.app_name,  # 从配置中读取项目名称，显示在接口文档页面
    debug=settings.debug,  # 从配置中读取是否开启调试模式
)
```

同时在文件开头增加：

```python
from app.core.config import settings  # 导入项目配置对象，读取项目名、调试开关等配置
```

### 1. 为什么要这样改

原来：

```python
app = FastAPI()
```

也能运行。

但是项目名、调试开关等信息都没有从配置中心读取。

现在：

```python
title=settings.app_name
debug=settings.debug
```

表示 `main.py` 不把配置写死，而是从 `app/core/config.py` 中读取。

一句话理解：

```text
main.py 负责启动应用
config.py 负责集中管理配置
```

这样以后要改项目名、运行环境、数据库地址、上传目录等配置，不需要到处改代码。

### 2. 这行 import 怎么理解

代码：

```python
from app.core.config import settings
```

拆开看：

```text
from             Python 保留字，表示从哪里导入
app.core.config  我们项目里的模块路径，对应 app/core/config.py
import           Python 保留字，表示导入
settings         config.py 里创建好的配置对象
```

意思是：

```text
从 app/core/config.py 这个文件里，把 settings 配置对象拿过来使用。
```

### 3. 哪些是固定写法，哪些是我们自己定义的

代码：

```python
app = FastAPI(
    title=settings.app_name,
    debug=settings.debug,
)
```

拆开理解：

```text
app       我们自己起的变量名，FastAPI 项目里通常叫 app
FastAPI   框架提供的类名，固定来自 fastapi 库
title     FastAPI 支持的参数名，不是我们随便起的
debug     FastAPI 支持的参数名，不是我们随便起的
settings  我们项目中定义的配置对象
app_name  我们在 Settings 类中定义的配置字段
debug     我们在 Settings 类中定义的配置字段
```

注意：这里有两个 `debug`。

第一个：

```python
debug=
```

是 FastAPI 支持的参数名。

第二个：

```python
settings.debug
```

是我们配置对象里的字段。

### 4. FastAPI 是什么

FastAPI 是一个 Python Web 后端框架。

一句话理解：

```text
FastAPI = 帮我们用 Python 写网站接口/API 的工具
```

它负责：

- 接收浏览器或客户端发来的 HTTP 请求。
- 根据访问路径找到对应的 Python 函数。
- 执行函数。
- 把函数返回值转换成 HTTP 响应。
- 自动生成接口文档页面。

例如：

```python
@app.get("/health")
def health_check():
    return {"status": "ok"}
```

意思是：

```text
当浏览器用 GET 请求访问 /health 时，执行 health_check 函数。
```

### 5. /docs 自动文档页

今天访问了：

```text
http://127.0.0.1:8000/docs
```

这是 FastAPI 自动生成的接口文档页面。

页面上显示：

```text
pyshare
```

说明这句配置生效了：

```python
title=settings.app_name
```

页面中还能看到：

```text
GET /health  Health Check
```

说明 FastAPI 已经识别到了 `/health` 接口。

其中 `Health Check` 是 FastAPI 根据函数名：

```python
health_check
```

自动转换出来的显示名称。

### 6. 今天的验证结果

运行命令：

```bash
uvicorn app.main:app --reload
```

访问：

```text
http://127.0.0.1:8000/docs
```

验证结果：

- 自动文档页面可以打开。
- 页面标题显示 `pyshare`。
- `/health` 接口出现在文档里。
- 说明 `main.py` 已经成功接入 `settings` 配置对象。

### 7. 下次继续前要做

下次开机后，先确认状态：

```bash
cd /Users/lucatyan/work/python/pyshare
git status
```

如果看到 `app/main.py` 和 `docs/learning-notes.md` 有改动，说明今天这次内容还没有提交。

下次可以先提交：

```bash
git add app/main.py docs/learning-notes.md
git commit -m "接入 FastAPI 应用配置"
git push
```

## 14. 路由拆分：把 /health 从 main.py 拆出去

今天学习了路由拆分。

一句话理解：

```text
main.py 只负责创建应用和组装路由
routers/*.py 负责按功能保存具体接口
```

### 1. 为什么要路由拆分

最开始 `/health` 直接写在 `app/main.py` 里：

```python
@app.get("/health")
def health_check():
    return {"status": "ok"}
```

现在只有一个接口时，这样写没问题。

但后面项目会有很多接口：

```text
注册
登录
上传文件
下载文件
删除文件
生成分享链接
访问分享链接
```

如果全部写在 `main.py`，文件会越来越乱。

所以真实项目通常会拆成：

```text
app/
  main.py
  routers/
    health.py
    auth.py
    files.py
    shares.py
```

### 2. 新建 health 路由文件

今天新建了：

```text
app/routers/health.py
```

完整代码：

```python
from fastapi import APIRouter  # 导入 APIRouter，用来创建一组路由


router = APIRouter()  # 创建一个路由对象，后面的接口先挂到这个 router 上


@router.get("/health")  # 注册一个 GET 接口，访问地址是 /health
def health_check():  # 定义接口处理函数，访问 /health 时会执行这个函数
    return {"status": "ok"}  # 返回一个字典，FastAPI 会自动转换成 JSON 响应
```

### 3. APIRouter 是什么

`APIRouter` 是 FastAPI 提供的路由工具。

可以先理解成：

```text
APIRouter = 一个小路由器，用来管理一组相关接口
```

以前写法：

```python
@app.get("/health")
```

表示直接把接口挂到主应用 `app` 上。

现在写法：

```python
@router.get("/health")
```

表示先把接口挂到 `router` 这个小路由器上。

最后再由 `main.py` 把这个小路由器挂到主应用上。

### 4. main.py 如何挂载路由

在 `app/main.py` 中新增导入：

```python
from app.routers import health  # 导入健康检查路由模块
```

这句的意思是：

```text
从 app/routers 文件夹中导入 health.py 这个模块。
```

然后新增：

```python
app.include_router(health.router)  # 把健康检查路由挂载到 FastAPI 主应用上
```

这句的意思是：

```text
把 health.py 里的 router 接到主应用 app 上。
```

### 5. 旧代码为什么注释保留

今天没有直接删除 `main.py` 里的旧 `/health` 代码，而是注释保留：

```python
# 下面是旧写法：直接在 main.py 中注册 /health 接口。
# 现在已经把 /health 拆到 app/routers/health.py，所以这里先注释保留学习记录。
# @app.get("/health")  # 注册一个 GET 接口，访问地址是 /health
# def health_check():  # 定义接口处理函数，访问 /health 时会执行这个函数
#     return {"status": "ok"}  # 返回一个字典，FastAPI 会自动转换成 JSON 响应
```

原因：

```text
这是学习阶段，保留旧写法可以看清楚代码从 main.py 迁移到 routers/health.py 的过程。
```

以后项目成熟后，可以再删除旧注释。

### 6. 拆分后的访问链路

现在访问：

```text
http://127.0.0.1:8000/health
```

实际链路是：

```text
浏览器访问 /health
        ↓
main.py 中的 app.include_router(health.router)
        ↓
app/routers/health.py 中的 router
        ↓
health_check()
        ↓
return {"status": "ok"}
```

### 7. 今天的验证结果

运行：

```bash
uvicorn app.main:app --reload
```

浏览器访问：

```text
http://127.0.0.1:8000/health
```

看到：

```json
{"status":"ok"}
```

说明路由拆分成功，`main.py` 能正确加载 `app/routers/health.py`。

### 8. 今天结束前的 Git 操作

今天涉及的文件：

```text
app/main.py
app/routers/health.py
docs/learning-notes.md
```

建议提交：

```bash
git add app/main.py app/routers/health.py docs/learning-notes.md
git commit -m "拆分健康检查路由"
git push
```

## 15. FastAPI 框架本身在哪里

今天明确了一个重要概念：

```text
FastAPI 框架本身不在 app/、docs/、docker/ 这些项目目录里。
```

FastAPI 是通过 `pip` 安装到当前项目的虚拟环境 `.venv` 中的第三方库。

大概位置类似：

```text
/Users/lucatyan/work/python/pyshare/.venv/lib/python.../site-packages/fastapi/
```

其中：

```text
.venv         当前项目自己的 Python 虚拟环境
site-packages Python 第三方库安装目录
fastapi       FastAPI 框架本体
```

项目代码中这句：

```python
from fastapi import FastAPI
```

意思是：

```text
从 .venv 中安装的 fastapi 包里，导入 FastAPI 这个类。
```

### FastAPI 会自动生成项目结构吗

不会。

FastAPI 不像某些框架那样强制生成固定项目结构。

例如：

```text
app/
docs/
docker/
tests/
```

这些不是 FastAPI 自动创建的。

这些是 `pyshare` 项目的目录结构，是按照真实后端项目习惯规划出来的。

当前项目中：

```text
app/      放 Python 应用代码
docs/     放学习笔记和项目文档
docker/   以后放 Docker、Nginx 等部署配置
tests/    以后放自动化测试
```

### app 目录里的几个子目录

```text
app/core/      项目配置，例如 config.py
app/db/        数据库相关代码，后面会继续学习
app/routers/   路由接口代码
app/services/  业务逻辑代码，后面会继续使用
```

一句话总结：

```text
FastAPI 提供 Web 框架能力；
项目目录结构由开发者自己组织；
我们当前的 app、docs、docker、tests 是 pyshare 项目结构，不是 FastAPI 框架本身。
```

## 16. 第一个 /files 文件管理入口

今天开始按照“迭代式 + 增量式开发”的思路推进文件管理功能。

本轮小目标：

```text
访问 /files 页面，能看到一个简单的文件管理页面标题。
```

暂时不做：

```text
数据库
用户注册
用户登录
对象存储
分享链接
```

先让核心链路一点点跑起来。

### 1. 新建文件管理路由

今天新建了：

```text
app/routers/files.py
```

完整代码：

```python
from fastapi import APIRouter  # 导入 APIRouter，用来创建文件管理相关路由


router = APIRouter()  # 创建文件管理路由对象，后面的 /files 页面会挂到这个 router 上


@router.get("/files")  # 注册一个 GET 接口，访问地址是 /files
def files_page():  # 定义文件管理页面处理函数，访问 /files 时会执行它
    return {"title": "文件管理页面"}  # 先返回一个简单 JSON，证明 /files 页面能访问
```

### 2. 在 main.py 中挂载 files 路由

在 `app/main.py` 中，把导入改成：

```python
from app.routers import files, health  # 导入文件管理路由模块和健康检查路由模块
```

然后新增：

```python
app.include_router(files.router)  # 把文件管理路由挂载到 FastAPI 主应用上
```

现在 `main.py` 会挂载两个路由：

```python
app.include_router(files.router)  # 把文件管理路由挂载到 FastAPI 主应用上
app.include_router(health.router)  # 把健康检查路由挂载到 FastAPI 主应用上
```

### 3. /files 的访问链路

现在访问：

```text
http://127.0.0.1:8000/files
```

实际链路是：

```text
浏览器访问 /files
        ↓
main.py 中的 app.include_router(files.router)
        ↓
app/routers/files.py 中的 router
        ↓
files_page()
        ↓
return {"title": "文件管理页面"}
```

### 4. 验证结果

运行：

```bash
uvicorn app.main:app --reload
```

访问：

```text
http://127.0.0.1:8000/files
```

Chrome 显示：

```json
{"title":"文件管理页面"}
```

说明 `/files` 路由已经成功接入。

### 5. Safari 中文乱码问题

今天看到 Safari 中中文 JSON 显示乱码，但 Chrome 显示正常。

判断：

```text
后端接口是正常的，主要是浏览器对中文 JSON 的编码显示差异。
```

当前阶段不需要深挖。

后面我们改成返回 HTML 页面，或者明确响应编码后，这类问题会自然解决。

### 6. 今天涉及的文件

```text
app/main.py
app/routers/files.py
docs/learning-notes.md
```

另外：

```text
app/db/models.py
```

是之前数据库学习时创建的文件，目前先保留，但暂时不继续数据库。

### 7. 今天结束前的 Git 操作

建议提交：

```bash
git add app/main.py app/routers/files.py docs/learning-notes.md
git commit -m "添加文件管理入口"
git push
```

如果要暂时保留数据库草稿文件但不提交，可以不要把 `app/db/models.py` 加入本次提交。
