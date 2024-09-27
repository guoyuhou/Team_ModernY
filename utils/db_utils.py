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

def get_dev_process():
    """
    获取开发流程
    :return: 开发流程列表
    """
    return list(db.dev_process.find({}, {"_id": 0}))

def get_learning_resources():
    """
    获取学习资源
    :return: 学习资源列表
    """
    return list(db.learning_resources.find({}, {"_id": 0}))

def add_learning_resource(resource):
    """
    添加新的学习资源
    :param resource: 学习资源字典
    :return: 插入的文档ID
    """
    return db.learning_resources.insert_one(resource).inserted_id

def update_team_info(new_info):
    """
    更新团队信息
    :param new_info: 新的团队信息字典
    :return: 更新结果
    """
    return db.team_info.update_one({}, {"$set": new_info})

def delete_learning_resource(resource_id):
    """
    删除学习资源
    :param resource_id: 资源ID
    :return: 删除结果
    """
    return db.learning_resources.delete_one({"_id": resource_id})

def get_latest_updates():
    """
    获取最新动态
    :return: 最新动态列表
    """
    return list(db.updates.find({}, {"_id": 0}).sort("date", -1).limit(5))
