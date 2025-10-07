from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

# 用户基础模型（共享字段）
class UserBase(BaseModel):
    username: str
    email: EmailStr

# 创建用户时使用的模型
class UserCreate(UserBase):
    password: str

# 更新用户时使用的模型
class UserUpdate(UserBase):
    is_active: Optional[bool] = None

# 从数据库读取用户时使用的模型，包含所有字段
class User(UserBase):
    id: int
    is_active: bool
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True  # 允许从ORM模型直接转换为Pydantic模型

# 登录请求模型
class UserLogin(BaseModel):
    username: str
    password: str

# 登录响应模型
class Token(BaseModel):
    access_token: str
    token_type: str

# Token数据模型
class TokenData(BaseModel):
    username: Optional[str] = None