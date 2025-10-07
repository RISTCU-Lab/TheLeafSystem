from db.database import engine, Base, get_db
from sqlalchemy.orm import Session
import time

# 初始化数据库
def init_database():
    print("正在尝试连接到PostgreSQL数据库...")
    
    # 尝试连接到数据库并创建表
    try:
        # 创建所有表
        Base.metadata.create_all(bind=engine)
        print("数据库表创建成功！")
        
        # 测试数据库会话连接
        print("正在测试数据库会话连接...")
        db: Session
        for db in get_db():
            try:
                # 执行简单查询以验证连接
                result = db.execute("SELECT version()")
                version = result.scalar_one_or_none()
                print(f"成功连接到PostgreSQL数据库！")
                print(f"PostgreSQL版本: {version}")
                break
            except Exception as e:
                print(f"数据库会话连接失败: {e}")
                time.sleep(2)  # 等待2秒后重试
    except Exception as e:
        print(f"数据库初始化失败: {e}")
        print("请检查以下几点：")
        print("1. PostgreSQL服务器是否正在运行")
        print("2. 用户名和密码是否正确")
        print("3. 数据库是否存在")
        print("4. 网络连接是否正常")
        return False
    
    print("数据库初始化完成！")
    return True

if __name__ == "__main__":
    init_database()