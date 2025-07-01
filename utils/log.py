# log.py
import logging
import os
from datetime import datetime

def setup_logger(log_dir="logs", log_file_prefix="test"):
    os.makedirs(log_dir, exist_ok=True)
    log_filename = os.path.join(log_dir, f"{log_file_prefix}_{datetime.now():%Y%m%d}.log")

    logger = logging.getLogger("selenium_demo")
    logger.setLevel(logging.INFO)

    # 重要！清掉 handler，避免多次導致 console handler 不生效
    if logger.hasHandlers():
        logger.handlers.clear()

    # Console handler
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    # File handler
    fh = logging.FileHandler(log_filename, encoding='utf-8')
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    return logger

logger = setup_logger()
