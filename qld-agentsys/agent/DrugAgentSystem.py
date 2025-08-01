# agent_system.py

from smolagents.agents import CodeAgent
from smolagents import LiteLLMModel, DuckDuckGoSearchTool, WikipediaSearchTool, HfApiModel
from sentence_transformers import SentenceTransformer
from pymongo import MongoClient
from agent.model import get_model, ModelName
from config.settings import (
    MONGODB_URI,
    COLLECTION_THUOC_INFO,
    MODEL_VN_EMBEDDING,
    OLLAMA_LOCAL_HOST
)
from agent.agent_prompt.core_agent import INIT_PLANNING_PROMPT as PLANNING_CORE_PROMPT
from agent.agent_prompt.retrieval_agent import INIT_PLANNING_PROMPT as PLANNING_DB
from agent.agent_tools.common_tools import (
    translate_vi_to_en_keep_names,
    db_drug_search,
    semantic_search,
    collection as db_collection,
    embedding_model as embedding_model_static,
    llm_translator as llm_translator_static
)


class DrugAgentSystem:
    def __init__(self):
        # Khởi tạo mô hình mặc định
        # self.model_main = get_model(ModelName.OLLAMA_DEEPSEEK_R1_14B)
        self.model_main = get_model(ModelName.GOOGLE_GEMINI_20_FLASH)
        self.model_formatter = get_model(ModelName.OLLAMA_PHOGPT4B)
        self.model_search = get_model(ModelName.OLLAMA_LLAMA3)
        # Khởi tạo các agents
        self.agent_web = CodeAgent(
            tools=[DuckDuckGoSearchTool(), WikipediaSearchTool()],
            model=self.model_search,
            max_steps=1,
            name="web_retrieval_agent",
            description="Agent responsible for retrieving drug information from the internet."
        )

        self.agent_db = CodeAgent(
            tools=[db_drug_search, semantic_search],
            model=self.model_search,
            max_steps=1,
            name="drug_retrieval_agent",
            description="Retrieves drug info from MongoDB using exact or semantic search."
        )
        self.agent_db.prompt_templates["planning"]["initial_plan"] = PLANNING_DB
    
        self.agent_orchestrator = CodeAgent(
            tools=[],
            model=self.model_main,
            max_steps=2,
            verbosity_level=2,
            name="drug_orchestrator_agent",
            managed_agents=[self.agent_db, self.agent_web]
        )
        self.agent_orchestrator.prompt_templates["planning"]["initial_plan"] = PLANNING_CORE_PROMPT
    def switch_model(self, model_name_main:str = ModelName.OLLAMA_DEEPSEEK_R1_14B, model_name_formatter: str = ModelName.OLLAMA_PHOGPT4B, model_name_search: str= ModelName.OLLAMA_LLAMA3):
        """
        Thay đổi mô hình cho các agent dựa trên tên mô hình.
        
        :param model_name_main: Tên mô hình cho agent orchestrator
        :param model_name_formatter: Tên mô hình cho model_formatter
        :param model_name_search: Tên mô hình cho các agent tìm kiếm
        """
        self.model_main = get_model(model_name_main)
        self.model_formatter = get_model(model_name_formatter)
        self.model_search = get_model(model_name_search)
        
        self.agent_web.model = self.model_search
        self.agent_db.model = self.model_search  
        self.agent_orchestrator.model = self.model_main


    def run(self, query: str) -> str:
        return self.agent_orchestrator.run(
            task=f"Question: {query}. Answer in Vietnamese.",
            reset=True
        )
    def question(self, query: str) -> str:
        """
        Xử lý truy vấn người dùng cuối:
        - Gọi agent chính để truy xuất dữ liệu
        - Format lại kết quả bằng LLM để dễ hiểu hơn với người dùng cuối
        """
        final = None
        for s in self.agent_orchestrator.run(task=query, stream=True):
            final = getattr(s, "final_answer", final)

        # prompt = (
        #     f"Hãy viết lại câu trả lời một cách rõ ràng, dễ hiểu dựa trên cặp câu hỏi - trả lời sau:\n"
        #     f"Câu hỏi: {query}\n"
        #     f"Trả lời: {final}\n"
        #     "Viết lại câu trả lời cho người dùng:"
        # )

        # messages = [
        #     {"role": "user", "content": prompt}
        # ]

        # response = self.model_formatter(messages)

        # print("PhoGPT-Answer: " + response.content)
        return final
