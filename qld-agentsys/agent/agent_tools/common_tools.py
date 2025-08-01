from smolagents.tools import tool
from sentence_transformers import SentenceTransformer
from pymongo import MongoClient
from smolagents import LiteLLMModel
from typing import List, Dict

from config.settings import (
    MONGODB_URI,
    COLLECTION_THUOC_INFO,
    MODEL_VN_EMBEDDING,
    DEFAULT_DB_NAME,
    COLLECTION_THUOC_CONGDUNG
)

# === Shared Instances ===
client = MongoClient(MONGODB_URI)
collection = client[DEFAULT_DB_NAME][COLLECTION_THUOC_INFO]
congdung_collection = client[DEFAULT_DB_NAME][COLLECTION_THUOC_CONGDUNG]

embedding_model = SentenceTransformer(MODEL_VN_EMBEDDING)

llm_translator = LiteLLMModel(
    model_id="gpt-3.5-turbo",
    api_base="https://api.openai.com/v1",
    custom_llm_provider="openai",
    flatten_messages_as_text=True
)

# === Tool: Translate Vietnamese to English while keeping names ===
@tool
def translate_vi_to_en_keep_names(text: str) -> str:
    """
    Translate Vietnamese to English, but preserve all proper nouns such as drug names or brand names.

    Args:
        text (str): Input text in Vietnamese.

    Returns:
        str: Translated English text with names kept intact.
    """
    prompt = (
        "Translate the following Vietnamese text to English. "
        "Do NOT translate any proper nouns such as drug names, brand names or organization names.\n\n"
        f"Text:\n{text}\n\n"
        "English translation (keep proper nouns intact):"
    )
    return llm_translator.invoke(prompt)

# === Tool: Fuzzy name search in MongoDB ===
@tool
def db_drug_search(name: str) -> str:
    """
    Search drug information in MongoDB using partial name match.

    Args:
        name (str): Approximate drug name.

    Returns:
        str: Drug information or not-found message.
    """
    result = collection.find_one(
        {"tenThuoc": {"$regex": name, "$options": "i"}},
        {"projection": {"embedding": 0, "fulltext": 0}}
    )
    return result.get("fulltext", "Không tìm thấy thông tin thuốc phù hợp.") if result else "Không tìm thấy thông tin thuốc phù hợp."

# === Tool: Semantic vector search in MongoDB ===
@tool
def semantic_search(query: str, top_k: int = 3) -> List[Dict]:
    """
    Semantic search using vector similarity to find related drug documents.

    Args:
        query (str): User natural language query.
        top_k (int): Number of top results to return.

    Returns:
        List[Dict]: List of documents (excluding embeddings and raw fulltext).
    """
    query_vector = embedding_model.encode(query).tolist()
    pipeline = [
        {
            "$vectorSearch": {
                "index": "vector_index",
                "path": "embedding",
                "queryVector": query_vector,
                "numCandidates": 100,
                "limit": top_k
            }
        },
        {"$project": {"embedding": 0, "fulltext": 0}},
    ]
    results = list(collection.aggregate(pipeline))
    return [
        {k: v for k, v in doc.items() if k not in ["embedding", "fulltext"]}
        for doc in results
    ]

# === Tool: Semantic vector search in MongoDB ===
@tool
def congdung_semantic_search(query: str, top_k: int = 1) -> List[Dict]:
    """
    Perform semantic search to retrieve drug usage (indication) information using vector similarity.

    Args:
        query (str): A natural language query related to drug usage or indications.
        top_k (int): The number of most relevant results to return.

    Returns:
        List[Dict]: A list of drug-related documents containing usage information (indications),
        excluding embedding vectors.
    """

    query_vector = embedding_model.encode(query).tolist()
    pipeline = [
        {
            "$vectorSearch": {
                "index": "vector_index",
                "path": "embedding",
                "queryVector": query_vector,
                "numCandidates": 100,
                "limit": top_k
            }
        },
        {"$project": {"embedding": 0, "congdung": 1}},
    ]
    results = list(congdung_collection.aggregate(pipeline))
    return [
        {k: v for k, v in doc.items() if k in ["congdung"]}
        for doc in results
    ]
