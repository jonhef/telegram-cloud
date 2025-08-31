import os
from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")

CONFIG_FILE = os.getenv("CONFIG")

CHUNK_SIZE = 1024 * 1024 * 1024