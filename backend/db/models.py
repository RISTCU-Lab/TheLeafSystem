from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func
from .database import Base

# 用户模型
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    hashed_password = Column(String(100), nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

# 你可以根据需要添加更多模型
# 例如：
# class Item(Base):
#     __tablename__ = "items"
#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String(100), index=True)
#     description = Column(String)
#     owner_id = Column(Integer, ForeignKey("users.id"))