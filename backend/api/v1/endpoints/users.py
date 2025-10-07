from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from db.database import get_db
from db import models
from schemas import user as user_schemas

router = APIRouter(
    prefix="/users",
    tags=["users"],
)

# 创建用户
@router.post("/", response_model=user_schemas.User)
def create_user(user: user_schemas.UserCreate, db: Session = Depends(get_db)):
    # 检查用户名是否已存在
    db_user = db.query(models.User).filter(models.User.username == user.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    # 检查邮箱是否已存在
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    # 创建新用户（注意：实际应用中应该对密码进行哈希处理）
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(username=user.username, email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# 获取用户列表
@router.get("/", response_model=List[user_schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = db.query(models.User).offset(skip).limit(limit).all()
    return users

# 获取单个用户
@router.get("/{user_id}", response_model=user_schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

# 更新用户
@router.put("/{user_id}", response_model=user_schemas.User)
def update_user(user_id: int, user: user_schemas.UserUpdate, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    # 更新用户信息
    if user.username:
        db_user.username = user.username
    if user.email:
        db_user.email = user.email
    if user.is_active is not None:
        db_user.is_active = user.is_active
    db.commit()
    db.refresh(db_user)
    return db_user

# 删除用户
@router.delete("/{user_id}", response_model=user_schemas.User)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(db_user)
    db.commit()
    return db_user