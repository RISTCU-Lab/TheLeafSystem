from fastapi import APIRouter
from .endpoints import users

# 创建v1版本的主路由器
api_router = APIRouter(prefix="/api/v1")

# 包含各个端点路由
api_router.include_router(users.router)

# 你可以根据需要添加更多端点路由
# 例如：
# from .endpoints import items
# api_router.include_router(items.router)