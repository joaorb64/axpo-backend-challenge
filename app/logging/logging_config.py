import logging
from logging.handlers import RotatingFileHandler
import sys
from app.settings import settings

logger = logging.getLogger()
logger.setLevel(settings.log_level)

# Console
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.INFO)
console_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
console_handler.setFormatter(console_formatter)
logger.addHandler(console_handler)
