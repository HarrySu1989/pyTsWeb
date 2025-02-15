import logging
from logging.handlers import RotatingFileHandler
from datetime import datetime
from flask import session

# 配置日志
def setup_logging():
    # 创建日志记录器
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)  # 设置日志级别为 DEBUG

    # 创建日志格式化器
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(module)s - %(funcName)s - %(lineno)d - %(message)s')

    # 创建文件处理器，按文件大小分割日志
    file_handler = RotatingFileHandler('app.log', maxBytes=1024 * 1024, backupCount=5)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    # 创建控制台处理器
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)

    # 将处理器添加到日志记录器
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

# 获取日志记录器
logger = setup_logging()

def add_log(param):
    try:
        user = session.get("user_id")
        logger.info(f"[{user}]{param}")
    except Exception as e:
        logger.error(f"记录日志时出错: {str(e)}", exc_info=True)

def add_log_b(param):
    try:
        logger.info(f"{param}")
    except Exception as e:
        logger.error(f"记录日志时出错: {str(e)}", exc_info=True)