import pymongo
from config import DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWORD

# 创建MongoDB客户端
client = pymongo.MongoClient(f"mongodb://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/")
db = client[DB_NAME]

def get_team_info():
    """
    获取团队信息
    :return: 团队信息字典
    """
    return db.team_info.find_one({}, {"_id": 0})

def get_latest_updates():
    """
    获取最新动态
    :return: 最新动态列表
    """
    return list(db.updates.find({}, {"_id": 0}).sort("date", -1).limit(5))

# 其他数据库操作函数...
