# pyshare

一个基于 FastAPI 的文件分享项目。

## 项目结构

```text
pyshare/
├── app/
│   ├── core/       # 项目配置、环境变量、安全相关代码
│   ├── db/         # 数据库连接、数据模型、初始化逻辑
│   ├── routers/    # API 路由
│   └── services/   # 业务逻辑
├── .env.example    # 环境变量示例
├── .gitignore      # Git 忽略规则
├── requirements.txt
└── README.md
```

## 本地开发

创建虚拟环境：

```bash
python -m venv .venv
```

启用虚拟环境：

```bash
source .venv/bin/activate
```

安装依赖：

```bash
pip install -r requirements.txt
```

复制环境变量文件：

```bash
cp .env.example .env
```

## 环境变量

`.env.example` 是示例配置文件，真实运行时使用 `.env`。

常用配置：

```text
APP_NAME=pyshare
APP_ENV=development
DEBUG=true
HOST=127.0.0.1
PORT=8000
DATABASE_URL=sqlite:///./pyshare.sqlite3
SECRET_KEY=change-me
UPLOAD_DIR=uploads
MAX_UPLOAD_SIZE_MB=100
```

注意：`.env` 里可能包含密码、密钥等敏感信息，不要提交到 Git。

## 运行项目

项目入口文件还没有创建。后续添加 `app/main.py` 后，可以使用类似命令启动：

```bash
uvicorn app.main:app --reload
```

启动后通常访问：

```text
http://127.0.0.1:8000
```

## 当前状态

目前已完成项目基础目录、依赖文件、环境变量示例和 Git 忽略规则。下一步通常是创建 FastAPI 入口文件 `app/main.py`，再逐步添加路由、数据库和文件上传功能。
