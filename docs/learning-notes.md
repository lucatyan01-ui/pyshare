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
