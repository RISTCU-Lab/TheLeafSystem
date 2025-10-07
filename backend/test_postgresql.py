import os
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

# 获取数据库配置
DATABASE_URL = os.getenv("DATABASE_URL")

print(f"尝试连接到数据库: {DATABASE_URL}")

# 使用psycopg2cffi直接连接数据库
try:
    # 解析数据库URL
    import re
    pattern = r'postgresql://(\\w+):(.*)@(\\w+\\.\\w+|\\d+\\.\\d+\\.\\d+\\.\\d+):(\\d+)/(\\w+)'
    match = re.match(pattern, DATABASE_URL)
    if match:
        username, password, host, port, database = match.groups()
        print(f"解析到的连接信息：")
        print(f"- 用户名: {username}")
        print(f"- 主机: {host}")
        print(f"- 端口: {port}")
        print(f"- 数据库: {database}")
        
        # 尝试导入psycopg2cffi
        print("\n正在导入psycopg2cffi...")
        import psycopg2cffi
        print("成功导入psycopg2cffi!")
        
        # 尝试连接数据库
        print("\n正在尝试连接到PostgreSQL数据库...")
        try:
            conn = psycopg2cffi.connect(
                dbname=database,
                user=username,
                password=password,
                host=host,
                port=port
            )
            print("成功连接到PostgreSQL数据库！")
            
            # 创建一个游标对象
            cursor = conn.cursor()
            
            # 执行简单的查询
            print("\n执行测试查询：SELECT version()")
            cursor.execute("SELECT version()")
            version = cursor.fetchone()[0]
            print(f"PostgreSQL版本: {version}")
            
            # 关闭游标和连接
            cursor.close()
            conn.close()
            print("\n连接已关闭。")
            
        except Exception as e:
            print(f"数据库连接失败: {e}")
            print("请检查以下几点：")
            print("1. PostgreSQL服务器是否正在运行")
            print("2. 用户名和密码是否正确")
            print("3. 数据库是否存在")
            print("4. 网络连接是否正常")
    else:
        print("无法解析数据库URL格式")

except Exception as e:
    print(f"发生错误: {e}")

print("\n测试完成。")