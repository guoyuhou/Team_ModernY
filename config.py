# 数据库配置
DB_HOST = "localhost"
DB_PORT = 27017
DB_NAME = "team_platform"
DB_USER = "admin"
DB_PASSWORD = "your_password_here"

# RabbitMQ配置
RABBITMQ_HOST = "localhost"
RABBITMQ_PORT = 5672

# 其他配置项
DEBUG = True
SECRET_KEY = "your_secret_key_here"

# 应用程序设置
APP_NAME = "团队内部平台"
APP_VERSION = "1.0.0"

# 文件上传设置
UPLOAD_FOLDER = "./uploads"
ALLOWED_EXTENSIONS = {"txt", "pdf", "png", "jpg", "jpeg", "gif"}

# 分页设置
ITEMS_PER_PAGE = 20

# 日志设置
LOG_LEVEL = "INFO"
LOG_FILE = "app.log"

# API设置
API_BASE_URL = "/api/v1"

# 邮件设置
MAIL_SERVER = "smtp.example.com"
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USERNAME = "your_email@example.com"
MAIL_PASSWORD = "your_email_password"

# 时区设置
TIMEZONE = "Asia/Shanghai"
