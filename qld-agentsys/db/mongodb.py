# db/mongodb.py

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from sentence_transformers import SentenceTransformer
from config.settings import COLLECTION_THUOC_INFO, MODEL_VN_EMBEDDING
from services.crawler import (
    crawl_thuoc_items,
    crawl_nguyenlieu_items,
    crawl_taduoc_items
)
from services.crawler import crawl_thuoc_detail_items
# services/congdung.py
from smolagents import LiteLLMModel, DuckDuckGoSearchTool
from smolagents.agents import CodeAgent
from config.settings import MODEL_VN_EMBEDDING, COLLECTION_THUOC_CONGDUNG, GEMINI_API_KEY

class MongoDB:
    def __init__(self, uri: str):
        self.uri = uri
        self.client = None
        self.model_embedding = SentenceTransformer(MODEL_VN_EMBEDDING)

    def connect(self):
        try:
            self.client = MongoClient(self.uri, server_api=ServerApi('1'))
            self.client.admin.command('ping')
            print("✅ Kết nối MongoDB thành công!")
        except Exception as e:
            print("❌ Kết nối MongoDB thất bại:", e)
            self.client = None

    def disconnect(self):
        if self.client:
            self.client.close()
            print("🔌 Đã ngắt kết nối MongoDB")

    def get_collection(self, db_name: str, collection_name: str = COLLECTION_THUOC_INFO):
        if not self.client:
            print("⚠️ Chưa kết nối MongoDB.")
            return None
        return self.client[db_name][collection_name]

    def _prepare_and_insert(self, db_name: str, data: list, loai: str, collection_name: str = COLLECTION_THUOC_INFO):
        if not self.client:
            print("⚠️ Chưa kết nối MongoDB.")
            return

        for item in data:
            item["loai"] = loai
            text = item.get("fulltext", "")
            vector = self.model_embedding.encode(text)
            item["embedding"] = vector.tolist()

        collection = self.get_collection(db_name, collection_name)
        result = collection.insert_many(data)
        print(f"✅ Đã thêm {len(result.inserted_ids)} bản ghi [{loai}] vào '{collection_name}'")

    def insert_thuoc(self, db_name: str, limit=100, batch_size=10):
        data = crawl_thuoc_items(limit=limit, batch_size=batch_size)
        self._prepare_and_insert(db_name, data, loai="thuoc")

    def insert_nguyenlieu(self, db_name: str, limit=100, batch_size=10):
        data = crawl_nguyenlieu_items(limit=limit, batch_size=batch_size)
        self._prepare_and_insert(db_name, data, loai="nguyenlieu")

    def insert_taduoc(self, db_name: str, limit=100, batch_size=10):
        data = crawl_taduoc_items(limit=limit, batch_size=batch_size)
        self._prepare_and_insert(db_name, data, loai="taduoc")
    def insert_thuoc_full(self, db_name: str, limit=100, batch_size=10,first_skip=0):
        """
        • Crawl thuốc (kèm nguyên liệu) → fulltext + embedding
        • Thêm vào collection mặc định
        • Gọi LLM lấy công dụng, lưu vào COLLECTION_THUOC_CONGDUNG
        """
        items = crawl_thuoc_detail_items(limit=limit, batch_size=batch_size,first_skip=first_skip)
        # insert thuốc + embedding
        self._prepare_and_insert(db_name, items, loai="thuoc")

        # lưu công dụng vào collection riêng
        for it in items:
            ten = it.get("tenThuoc")
            if ten:
                insert_congdung(self, db_name, ten)


# Khởi tạo LLM
model_gemini = LiteLLMModel(model_id="gemini/gemini-2.0-flash-exp",
                     api_key=GEMINI_API_KEY)
agent = CodeAgent(model=model_gemini, tools=[DuckDuckGoSearchTool()])

def fetch_congdung(ten_thuoc: str) -> str | None:
    """Hỏi LLM, trả về công dụng ngắn gọn"""
    q = f"Công dụng của thuốc {ten_thuoc} là gì? Trả lời bằng tiếng Việt. Nếu thông tin về công dụng thuốc có tên không chính xác, hãy trả lời là 'Không có thông tin về công dụng của thuốc {ten_thuoc}'."
    try:
        answer = agent.run(q)
        return answer.strip()
    except Exception as e:
        print("❌ Lỗi truy vấn công dụng:", e)
        return None

def insert_congdung(db: MongoDB, db_name: str, ten_thuoc: str):
    txt = fetch_congdung(ten_thuoc)
    if not txt:
        return
    vec = db.model_embedding.encode(txt).tolist()
    doc = {"congdung": txt, "embedding": vec}
    col = db.get_collection(db_name, COLLECTION_THUOC_CONGDUNG)
    col.insert_one(doc)
    print(f"✅ Đã lưu công dụng '{ten_thuoc}'")
