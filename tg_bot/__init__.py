# 2020 (c) KassemSYR.
import logging
import os

from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


logger.info("Loading Configurations...")

APP_ID = int(os.environ.get("APP_ID", 12345))
API_HASH = os.environ.get("API_HASH", "")
TOKEN = os.environ.get("TOKEN", "")