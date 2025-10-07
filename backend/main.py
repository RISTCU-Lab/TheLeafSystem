from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv

# 导入数据库模块
from db.database import engine, Base
from api.v1.routes import api_router

# 加载环境变量
load_dotenv()

# 创建FastAPI应用实例
app = FastAPI(
    title="TheLeafSystem API",
    description="Backend API for TheLeafSystem",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# 配置CORS，允许前端访问
origins = [
    "http://localhost",
    "http://localhost:5173",  # Vite默认端口
    "http://localhost:3000",  # 常见的React应用端口
    # 添加其他需要允许的源
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 初始化数据库表
@app.on_event("startup")
def startup_event():
    Base.metadata.create_all(bind=engine)

# 包含API路由
app.include_router(api_router)

# 根路由
@app.get("/")
def read_root():
    return {"message": "Welcome to TheLeafSystem API"}

# 如果直接运行此文件，启动开发服务器
if __name__ == "__main__":
    import uvicorn
    
    host = os.getenv("SERVER_HOST", "127.0.0.1")
    port = int(os.getenv("SERVER_PORT", "8000"))
    reload = os.getenv("DEBUG", "True").lower() == "true"
    
    uvicorn.run("main:app", host=host, port=port, reload=reload)