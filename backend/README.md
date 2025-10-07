# TheLeafSystem Backend

这是TheLeafSystem的后端API项目，使用FastAPI和SQLAlchemy构建。

## 项目结构

```
backend/
├── api/                 # API路由和端点
│   └── v1/              # API版本1
│       ├── endpoints/   # 各个API端点
│       └── routes.py    # 路由配置
├── db/                  # 数据库相关代码
│   ├── database.py      # 数据库连接配置
│   └── models.py        # 数据库模型定义
├── schemas/             # Pydantic模型（用于数据验证和序列化）
├── main.py              # 应用主入口
├── requirements.txt     # 项目依赖
├── .env                 # 环境变量配置
└── .gitignore           # Git忽略文件配置
```

## 快速开始

### 安装依赖

```bash
pip install -r requirements.txt
```

### 运行开发服务器

```bash
python main.py
```

或使用uvicorn直接运行：

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### API文档

启动服务器后，可以通过以下URL访问API文档：
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## 环境变量配置

在`.env`文件中配置以下环境变量：

```
# 数据库配置
DATABASE_URL=sqlite:///./leavesystem.db
# FastAPI配置
SERVER_HOST=0.0.0.0
SERVER_PORT=8000
# 开发模式
DEBUG=True
```

## 数据库迁移

本项目使用SQLAlchemy的元数据创建数据库表。启动应用时，会自动创建所有定义的表。

## 注意事项

- 本项目仅供开发和学习使用，在生产环境中应添加适当的安全措施，如密码哈希、身份验证和授权等。
- 生产环境中应使用生产级数据库，如PostgreSQL或MySQL。
- 生产环境中应禁用DEBUG模式。