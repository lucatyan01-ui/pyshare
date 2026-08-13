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

## 17. 让 /files 返回 HTML 页面

今天把 `/files` 从返回 JSON 升级成返回真正的 HTML 页面。

上一版返回：

```json
{"title":"文件管理页面"}
```

今天升级后，浏览器能看到页面：

```text
PyShare 文件管理
这里将显示上传、下载和删除文件的功能。
```

### 1. 新建模板文件

今天新建：

```text
app/templates/files.html
```

完整内容：

```html
<!DOCTYPE html>
<html lang="zh-CN">
    <head>
        <meta charset="utf-8">
        <title>PyShare 文件管理</title>
    </head>
    <body>
        <h1>PyShare 文件管理</h1>
        <p>这里将显示上传、下载和删除文件的功能。</p>
    </body>
</html>
```

其中：

```html
<meta charset="utf-8">
```

表示告诉浏览器用 UTF-8 编码显示页面，可以避免中文乱码。

### 2. Jinja2Templates

在 `app/routers/files.py` 中新增：

```python
from fastapi import APIRouter, Request  # 导入 APIRouter 和 Request，Request 用来把请求信息传给模板
from fastapi.templating import Jinja2Templates  # 导入 Jinja2Templates，用来返回 HTML 模板页面
```

然后创建模板工具对象：

```python
templates = Jinja2Templates(directory="app/templates")  # 指定 HTML 模板文件所在目录
```

一句话理解：

```text
告诉 FastAPI：以后 HTML 模板去 app/templates 目录里找。
```

### 3. TemplateResponse

今天把 `files_page()` 改成：

```python
@router.get("/files")  # 注册一个 GET 接口，访问地址是 /files
def files_page(request: Request):  # 定义文件管理页面处理函数，并接收浏览器请求对象
    return templates.TemplateResponse(  # 返回 HTML 模板响应
        "files.html",  # 指定要渲染的模板文件名
        {"request": request},  # 把 request 传给模板，这是 FastAPI 模板要求的
    )
```

含义：

```text
访问 /files 时，FastAPI 去 app/templates 目录中找到 files.html，并返回给浏览器。
```

这里的：

```python
{"request": request}
```

是 FastAPI 使用 Jinja2 模板时要求传入的内容。

### 4. jinja2 依赖

第一次运行时报错：

```text
AssertionError: jinja2 must be installed to use Jinja2Templates
```

原因：

```text
项目使用了 Jinja2Templates，但虚拟环境里还没有安装 jinja2。
```

解决：

```bash
pip install jinja2
```

并把依赖写进 `requirements.txt`：

```text
jinja2==3.1.6
```

这样以后换电脑或部署服务器时，执行：

```bash
pip install -r requirements.txt
```

就会自动安装 `jinja2`。

### 5. 今天验证结果

运行：

```bash
uvicorn app.main:app --reload
```

访问：

```text
http://127.0.0.1:8000/files
```

浏览器成功显示 HTML 页面：

```text
PyShare 文件管理
```

说明：

- `/files` 路由正常。
- `Jinja2Templates` 正常。
- `files.html` 模板正常。
- 中文编码正常。

### 6. 今天结束前的 Git 操作

今天涉及的文件：

```text
app/routers/files.py
app/templates/files.html
requirements.txt
docs/learning-notes.md
```

建议提交：

```bash
git add app/routers/files.py app/templates/files.html requirements.txt docs/learning-notes.md
git commit -m "让文件管理入口返回 HTML 页面"
git push
```

注意：

```text
app/db/models.py
```

仍然是之前数据库草稿，暂时保留但不提交。

## 18. 在 /files 页面添加上传表单

今天继续按“迭代式 + 增量式开发”的思路推进。

本轮小目标：

```text
在 /files 页面上看到文件选择框和上传按钮。
```

今天只做前端表单，不做真正上传。

真正接收文件的后端接口：

```text
POST /files/upload
```

下一轮再实现。

### 1. 修改 files.html

修改文件：

```text
app/templates/files.html
```

在说明文字下面加入：

```html
<!-- 文件上传表单：提交到后端 /files/upload 接口 -->
<form method="post" action="/files/upload" enctype="multipart/form-data">
    <!-- 文件选择框：name 是后端接收文件时使用的字段名 -->
    <input type="file" name="upload_file">
    <!-- 提交按钮：点击后把选择的文件发送给后端 -->
    <button type="submit">上传</button>
</form>
```

### 2. form 表单

`form` 表示 HTML 表单。

可以理解成：

```text
把用户输入或选择的数据打包后，提交给后端。
```

本项目里，表单负责把用户选择的文件提交给 FastAPI。

### 3. method="post"

代码：

```html
method="post"
```

意思是：

```text
用 POST 请求提交数据。
```

一般来说：

```text
GET   用来获取数据
POST  用来提交数据
```

上传文件属于提交数据，所以这里用 `POST`。

### 4. action="/files/upload"

代码：

```html
action="/files/upload"
```

意思是：

```text
点击上传按钮后，把表单数据提交到 /files/upload 这个后端地址。
```

目前这个后端接口还没有实现。

所以现在如果点击上传，可能会出现 `404 Not Found` 或 `405 Method Not Allowed`。

这是正常的，因为今天只完成页面表单。

### 5. enctype="multipart/form-data"

代码：

```html
enctype="multipart/form-data"
```

这是上传文件时必须写的重要属性。

一句话理解：

```text
告诉浏览器：这个表单里有文件，请用适合文件上传的格式提交。
```

如果不写这个，后端通常无法正确接收文件内容。

### 6. input type="file"

代码：

```html
<input type="file" name="upload_file">
```

含义：

```text
type="file"      显示文件选择框
name="upload_file"  后端接收文件时使用的字段名
```

后面 FastAPI 接收文件时，会使用同样的名字：

```python
upload_file
```

前端 `name` 和后端参数名要对应。

### 7. button type="submit"

代码：

```html
<button type="submit">上传</button>
```

含义：

```text
点击按钮后，提交整个表单。
```

### 8. 今天验证结果

运行：

```bash
uvicorn app.main:app --reload
```

访问：

```text
http://127.0.0.1:8000/files
```

页面成功显示：

```text
PyShare 文件管理
选取文件
上传
```

说明：

```text
/files 页面已经成功显示上传表单。
```

### 9. 今天结束前的 Git 操作

今天涉及文件：

```text
app/templates/files.html
docs/learning-notes.md
```

建议提交：

```bash
git add app/templates/files.html docs/learning-notes.md
git commit -m "添加文件上传表单"
git push
```

注意：

```text
app/db/models.py
```

仍然是数据库草稿，暂时不提交。

## 19. 接收上传文件并保存到本地 uploads 目录

今天实现了真正的文件上传保存。

本轮小目标：

```text
选择文件 -> 点击上传 -> FastAPI 接收文件 -> 保存到 uploads/ 目录
```

### 1. 创建 uploads 目录

在项目根目录创建：

```bash
mkdir -p uploads
```

完整路径：

```text
/Users/lucatyan/work/python/pyshare/uploads
```

这个目录用来临时保存用户上传的文件。

`.gitignore` 中已经有：

```gitignore
uploads/
```

所以上传的真实文件不会被提交到 GitHub。

这是正确的，因为用户上传文件属于运行数据，不属于项目源代码。

### 2. 导入 Path

在 `app/routers/files.py` 中新增：

```python
from pathlib import Path  # 导入 Path，用来处理文件和目录路径
```

`Path` 来自 Python 标准库 `pathlib`。

一句话理解：

```text
Path = Python 中更适合处理文件路径的工具。
```

例如：

```python
upload_dir = Path("uploads")
```

表示项目根目录下的 `uploads` 目录。

路径拼接：

```python
file_path = upload_dir / upload_file.filename
```

这里的 `/` 不是除法，而是 `Path` 提供的路径拼接写法。

例如：

```text
uploads/a.txt
```

### 3. 上传目录变量

在 `files.py` 中新增：

```python
upload_dir = Path("uploads")  # 指定上传文件保存目录
```

含义：

```text
把 uploads 目录保存到 upload_dir 变量中，后面保存文件时使用。
```

### 4. 接收上传文件

上传接口：

```python
@router.post("/files/upload")  # 注册一个 POST 接口，接收文件上传表单
def upload_file(upload_file: UploadFile = File(...)):  # 接收表单中 name="upload_file" 的文件
```

对应 HTML 表单：

```html
<input type="file" name="upload_file">
```

关键点：

```text
前端 name="upload_file"
后端参数 upload_file
```

这两个名字要对应。

`UploadFile` 表示 FastAPI 接收到的上传文件对象。

`File(...)` 告诉 FastAPI：

```text
这个参数来自 multipart/form-data 表单里的文件字段。
```

### 5. 保存文件代码

当前保存逻辑：

```python
@router.post("/files/upload")  # 注册一个 POST 接口，接收文件上传表单
def upload_file(upload_file: UploadFile = File(...)):  # 接收表单中 name="upload_file" 的文件
    file_path = upload_dir / upload_file.filename  # 拼出文件保存路径，例如 uploads/a.txt
    content = upload_file.file.read()  # 读取上传文件的全部内容
    file_path.write_bytes(content)  # 把文件内容写入服务器本地磁盘
    return {"filename": upload_file.filename, "saved_to": str(file_path)}  # 返回保存结果
```

逐行理解：

```python
file_path = upload_dir / upload_file.filename
```

拼出保存路径。

例如上传：

```text
python_file_share_50h_plan.md
```

保存路径就是：

```text
uploads/python_file_share_50h_plan.md
```

```python
content = upload_file.file.read()
```

读取上传文件的全部内容。

```python
file_path.write_bytes(content)
```

把读取到的内容写入本地磁盘。

```python
return {"filename": upload_file.filename, "saved_to": str(file_path)}
```

返回文件名和保存路径，方便验证。

### 6. 今天验证结果

上传文件：

```text
python_file_share_50h_plan.md
```

浏览器返回：

```json
{
  "filename": "python_file_share_50h_plan.md",
  "saved_to": "uploads/python_file_share_50h_plan.md"
}
```

终端执行：

```bash
ls uploads
```

看到：

```text
python_file_share_50h_plan.md
```

说明：

```text
文件已经真正保存到 uploads/ 目录。
```

### 7. 当前版本的限制

当前实现是学习版，功能已经跑通，但还不够安全和完整。

后面需要改进：

- 文件名安全处理，避免路径穿越。
- 文件重名处理，避免覆盖旧文件。
- 大文件不能一次性全部读入内存。
- 上传成功后跳回 /files 页面。
- 在 /files 页面显示文件列表。
- 后续再接入数据库记录文件信息。

### 8. 下次建议

下一步建议：

```text
在 /files 页面显示 uploads/ 目录里的文件列表。
```

这样上传后就能在页面看到已有文件。

### 9. 今天结束前的 Git 操作

今天涉及文件：

```text
app/routers/files.py
docs/learning-notes.md
```

建议提交：

```bash
git add app/routers/files.py docs/learning-notes.md
git commit -m "保存上传文件到本地目录"
git push
```

注意不要提交：

```text
uploads/
app/db/models.py
```

`uploads/` 是运行数据，已被 `.gitignore` 忽略。

`app/db/models.py` 仍然是数据库草稿，暂时不提交。

## 20. 在 /files 页面显示已上传文件列表

今天实现了文件列表显示。

本轮小目标：

```text
/files 页面能显示 uploads/ 目录中的文件名。
```

### 1. 后端读取 uploads 目录

在 `app/routers/files.py` 的 `files_page()` 中新增：

```python
files = [path.name for path in upload_dir.iterdir() if path.is_file()]  # 读取 uploads 目录中的文件名列表
```

这句是 Python 列表推导式。

普通写法等价于：

```python
files = []

for path in upload_dir.iterdir():
    if path.is_file():
        files.append(path.name)
```

含义：

```text
遍历 uploads 目录；
只保留文件，不要文件夹；
取每个文件的文件名；
组成一个列表。
```

### 2. for / in / if 语法

普通循环：

```python
for path in upload_dir.iterdir():
    ...
```

含义：

```text
从 upload_dir.iterdir() 里一个一个取东西；
每取出一个，临时叫 path。
```

条件判断：

```python
if path.is_file():
    ...
```

含义：

```text
如果 path 是文件，就执行缩进里的代码。
```

列表推导式结构：

```python
[要收集的结果 for 临时变量 in 数据来源 if 条件]
```

对应当前代码：

```python
[path.name for path in upload_dir.iterdir() if path.is_file()]
```

拆开：

```text
要收集的结果：path.name
临时变量：path
数据来源：upload_dir.iterdir()
条件：path.is_file()
```

### 3. path.name

`path.name` 的作用：

```text
从一个路径中取出最后的文件名或目录名。
```

例如：

```python
Path("uploads/a.txt").name
```

结果：

```text
a.txt
```

在本项目中，页面只需要显示文件名，不需要显示完整路径：

```text
uploads/python_file_share_50h_plan.md
```

所以使用：

```python
path.name
```

得到：

```text
python_file_share_50h_plan.md
```

### 4. 把 files 传给模板

原来：

```python
{"request": request}
```

现在：

```python
{"request": request, "files": files}
```

含义：

```text
把 request 和文件名列表 files 一起传给 files.html。
```

### 5. Jinja2 是什么

Jinja2 是 Python 模板引擎。

一句话理解：

```text
Jinja2 = 把 HTML 模板 + 后端数据 合成最终网页的工具。
```

后端数据：

```python
files = ["a.txt", "b.png"]
```

模板：

```html
{% for file in files %}
    <li>{{ file }}</li>
{% endfor %}
```

最终生成：

```html
<li>a.txt</li>
<li>b.png</li>
```

浏览器最终看到的是生成后的 HTML，不是 `{% for %}` 这些模板语法。

### 6. Jinja2 的两种常用语法

输出变量：

```html
{{ file }}
```

含义：

```text
把 file 的值显示到 HTML 页面。
```

控制语句：

```html
{% for file in files %}
{% endfor %}
```

含义：

```text
循环 files 列表。
```

注意：

```text
{% ... %} 是 Jinja2 模板语法，不是 HTML 原生语法，也不是完整 Python 代码。
```

它像 Python，但属于模板引擎语法。

### 7. 修改 files.html

在 `app/templates/files.html` 中新增：

```html
<h2>已上传文件</h2>

<!-- 文件列表：files 是后端传给模板的文件名列表 -->
<ul>
    {% for file in files %}
        <!-- 每循环一次，就显示一个文件名 -->
        <li>{{ file }}</li>
    {% endfor %}
</ul>
```

### 8. 今天验证结果

访问：

```text
http://127.0.0.1:8000/files
```

页面显示：

```text
已上传文件
- python_file_share_50h_plan.md
```

说明：

```text
后端成功读取 uploads 目录；
模板成功循环显示文件名；
/files 页面已经能展示已上传文件列表。
```

### 9. 下次建议

下一步建议：

```text
上传成功后自动跳回 /files 页面，而不是显示 JSON。
```

这样上传体验会更像真实网站。

### 10. 今天结束前的 Git 操作

今天涉及文件：

```text
app/routers/files.py
app/templates/files.html
docs/learning-notes.md
```

建议提交：

```bash
git add app/routers/files.py app/templates/files.html docs/learning-notes.md
git commit -m "显示已上传文件列表"
git push
```

注意不要提交：

```text
app/db/models.py
uploads/
```

## 二十一、上传成功后自动回到文件管理页面

### 1. 本次小目标

之前上传文件成功后，浏览器会停在 JSON 页面，例如：

```json
{"filename": "a.txt", "saved_to": "uploads/a.txt"}
```

这说明后端保存文件成功了，但用户体验不像真实网站。

本次目标：

```text
选择文件 -> 点击上传 -> 后端保存文件 -> 自动回到 /files 页面 -> 页面显示最新文件列表
```

### 2. 导入 RedirectResponse

在 `app/routers/files.py` 中新增：

```python
from fastapi.responses import RedirectResponse  # 导入重定向响应，用来让上传成功后跳回文件列表页面
```

说明：

```text
RedirectResponse 是“重定向响应”。
它不是返回 JSON，而是告诉浏览器跳转到另一个地址。
```

### 3. 保留旧代码，改成重定向

旧写法：

```python
return {"filename": upload_file.filename, "saved_to": str(file_path)}  # 返回保存结果
```

新写法：

```python
# 旧写法：上传成功后返回 JSON 数据，浏览器页面会停在 JSON 结果页。
# return {"filename": upload_file.filename, "saved_to": str(file_path)}  # 返回保存结果
return RedirectResponse(url="/files", status_code=303)  # 上传成功后重定向回文件列表页面
```

注意：

```text
函数执行到 return 就结束。
如果旧 return 不注释掉，新的 RedirectResponse 永远不会执行。
```

### 4. 303 是什么意思

```python
status_code=303
```

303 是 HTTP 状态码，完整含义是：

```text
303 See Other
```

在这个项目里可以理解成：

```text
你刚才用 POST 提交了上传文件；
服务器已经保存好了；
现在请浏览器改用 GET 请求访问 /files 页面。
```

这个写法适合表单提交成功后的跳转，也能避免刷新页面时重复提交表单。

### 5. 修复空文件上传问题

测试时出现过错误：

```text
IsADirectoryError: [Errno 21] Is a directory: 'uploads'
```

原因：

```text
没有选择文件就提交；
upload_file.filename 为空；
file_path = upload_dir / upload_file.filename 实际变成了 uploads；
程序试图把文件内容写入 uploads 这个目录，于是报错。
```

前端修复：

```html
<!-- 文件选择框：name 是后端接收文件时使用的字段名，required 表示必须选择文件才能提交 -->
<input type="file" name="upload_file" required>
```

说明：

```text
required 是 HTML 自带属性。
它表示这个输入框必填。
没有选择文件时，浏览器会拦住表单提交。
```

### 6. 本次验证结果

访问：

```text
http://127.0.0.1:8000/files
```

验证结果：

```text
不选择文件时，浏览器提示必须选择文件；
选择文件上传后，页面自动回到 /files；
已上传文件列表能看到新文件名。
```

本次已实现的完整流程：

```text
浏览器选择文件
-> 表单 POST 到 /files/upload
-> FastAPI 接收 UploadFile
-> 保存到本地 uploads 目录
-> RedirectResponse 返回 303
-> 浏览器 GET /files
-> Jinja2 模板显示最新文件列表
```

### 7. 下次建议

下一步建议：

```text
给文件名加下载链接，实现点击文件名下载文件。
```

这样项目的核心功能会从“上传 + 查看列表”推进到：

```text
上传 + 查看列表 + 下载
```

### 8. 本次结束前的 Git 操作

本次涉及文件：

```text
app/routers/files.py
app/templates/files.html
docs/learning-notes.md
```

建议提交：

```bash
git add app/routers/files.py app/templates/files.html docs/learning-notes.md
git commit -m "上传后重定向回文件列表"
git push
```

注意继续不要提交：

```text
app/db/models.py
uploads/
```

## 二十二、实现文件下载功能

### 1. 本次小目标

上一阶段已经实现：

```text
上传文件
显示文件列表
```

本次目标：

```text
点击文件名 -> 浏览器下载对应文件
```

这样项目核心功能变成：

```text
上传 + 查看列表 + 下载
```

### 2. 导入 FileResponse

在 `app/routers/files.py` 中修改导入：

```python
from fastapi.responses import FileResponse, RedirectResponse  # 导入文件下载响应和重定向响应
```

说明：

```text
FileResponse 用来把服务器上的文件返回给浏览器。
RedirectResponse 用来让浏览器跳转页面。
```

### 3. 新增下载接口

在 `app/routers/files.py` 中新增：

```python
@router.get("/files/download/{filename}")  # 注册一个 GET 接口，用来下载指定文件
def download_file(filename: str):  # filename 来自网址中的 {filename}，类型是字符串
    file_path = upload_dir / filename  # 拼出要下载的文件路径，例如 uploads/a.txt
    return FileResponse(path=file_path, filename=filename)  # 把服务器上的文件返回给浏览器下载
```

说明：

```text
/files/download/{filename} 中的 {filename} 是路径参数。
浏览器访问 /files/download/a.txt 时，FastAPI 会把 a.txt 传给 filename。
```

执行过程：

```text
浏览器请求 /files/download/a.txt
-> FastAPI 匹配 /files/download/{filename}
-> filename = "a.txt"
-> file_path = uploads/a.txt
-> FileResponse 返回文件内容
```

### 4. 把文件名变成下载链接

在 `app/templates/files.html` 中，把原来的普通文件名：

```html
<li>{{ file }}</li>
```

改成：

```html
<!-- 每循环一次，就把一个文件名显示成下载链接 -->
<li>
    <!-- href 是点击后访问的地址，{{ file }} 会被 Jinja2 替换成真实文件名 -->
    <a href="/files/download/{{ file }}">{{ file }}</a>
</li>
```

假设文件名是：

```text
a.txt
```

Jinja2 最终生成：

```html
<a href="/files/download/a.txt">a.txt</a>
```

### 5. 为什么点击文件名会触发 GET 请求

因为 HTML 中：

```html
<a href="/files/download/a.txt">a.txt</a>
```

`<a>` 是超链接标签，`href` 是点击后访问的地址。

浏览器规则：

```text
点击普通链接 <a href="...">，默认发起 GET 请求。
```

所以点击文件名会触发：

```text
GET /files/download/a.txt
```

对比：

```text
普通链接 a 标签 -> GET 请求
表单 method="post" -> POST 请求
```

### 6. 下载功能完整原理

完整流程：

```text
Jinja2 把文件名渲染成链接
-> 用户点击文件名
-> 浏览器 GET /files/download/文件名
-> FastAPI 从 URL 中取出 filename
-> 后端拼出 uploads/文件名
-> FileResponse 返回文件
-> 浏览器下载文件
```

关键理解：

```text
浏览器不是直接读取服务器 uploads 文件夹。
浏览器只能请求后端接口。
后端接口读取服务器文件，再把文件内容返回给浏览器。
```

### 7. 本次验证结果

访问：

```text
http://127.0.0.1:8000/files
```

验证：

```text
页面上的文件名已经变成可点击链接；
点击文件名后，浏览器可以下载对应文件。
```

### 8. 下次建议

下一步建议：

```text
增加删除文件功能。
```

这样核心功能会继续推进到：

```text
上传 + 查看列表 + 下载 + 删除
```

### 9. 本次结束前的 Git 操作

本次涉及文件：

```text
app/routers/files.py
app/templates/files.html
docs/learning-notes.md
```

建议提交：

```bash
git add app/routers/files.py app/templates/files.html docs/learning-notes.md
git commit -m "添加文件下载功能"
git push
```

注意继续不要提交：

```text
app/db/models.py
uploads/
```
