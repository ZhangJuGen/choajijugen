import os
import datetime

# ---------------- 项目路径相关 --------------------
# 项目路径
BasePath = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

# 请求模板存放地址
requestAddress = "api_yaml"

# 测试用例存放地址
testCaseAddress = "test_case"

# env存放地址
ENV = "conf/env.yaml"

# ---------------- 日志相关 --------------------
# 日志级别
LOG_LEVEL = 'debug'
LOG_STREAM_LEVEL = 'debug'  # 屏幕输出流
LOG_FILE_LEVEL = 'info'  # 文件输出流

# 日志文件命名
LOG_FILE_NAME = os.path.join(BasePath, 'logs', datetime.datetime.now().strftime('%Y-%m-%d') + '.log')

# ---------------- 数据库相关 --------------------
HOST = '172.22.9.5'
USER = 'root'
PASSWORD = 'hanyastar'
PORT = 3306
database = 'dns-ynjnrcpjfwpt-empty'
