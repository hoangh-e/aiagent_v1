import os
from dotenv import load_dotenv

load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI")

# API URLs
OLLAMA_LOCAL_HOST = os.getenv("OLLAMA_LOCAL_HOST")
DAV_API_URL_THUOC = os.getenv("DAV_API_URL_THUOC")
DAV_API_URL_TADUOC = os.getenv("DAV_API_URL_TADUOC")
DAV_API_URL_NGUYENLIEU = os.getenv("DAV_API_URL_NGUYENLIEU")
DAV_API_URL_NGUYENLIEU_BYSDKTHUOC = os.getenv("DAV_API_URL_NGUYENLIEU_BY_SDKTHUOC")

DAV_API_HEADERS = {
    "Content-Type": "application/json"
}

#DB
COLLECTION_THUOC_INFO = "thuoc_thongtin"
COLLECTION_THUOC_CONGDUNG = "thuoc_congdung"
DEFAULT_DB_NAME = "duoc_pham"

#models - names
MODEL_VN_EMBEDDING = "bkai-foundation-models/vietnamese-bi-encoder"

# API keys
HF_API_KEY = os.getenv("HF_API_KEY")
NGROK_API_KEY = os.getenv("NGROK_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")