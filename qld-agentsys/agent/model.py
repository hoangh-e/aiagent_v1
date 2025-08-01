from smolagents import LiteLLMModel
from config.settings import OLLAMA_LOCAL_HOST, GEMINI_API_KEY

# Enum các mô hình đã được định nghĩa
class ModelName:
    OLLAMA_DEEPSEEK_R1_14B = "deepseek-r1:14b"
    OLLAMA_PHOGPT4B = "vi-dominic/phogpt:4b"
    OLLAMA_LLAMA3 = "llama3"
    GOOGLE_GEMINI_15_FLASH = "gemini-1.5-flash"
    GOOGLE_GEMINI_20_FLASH = "gemini-2.0-flash-exp"
    GOOGLE_GEMINI_25_FLASH = "gemini-2.5-flash"
    GOOGLE_GEMINI_20_PRO = "gemini-2.0-pro"
    GOOGLE_GEMINI_25_PRO = "gemini-2.5-pro"


def get_model(model_name: str):
    match model_name:
        case ModelName.OLLAMA_DEEPSEEK_R1_14B:
            return LiteLLMModel(
                model_id=ModelName.OLLAMA_DEEPSEEK_R1_14B,
                api_base=OLLAMA_LOCAL_HOST,
                custom_llm_provider="ollama",
                flatten_messages_as_text=True,
            )
        case ModelName.OLLAMA_PHOGPT4B:
            return LiteLLMModel(
                model_id=ModelName.OLLAMA_PHOGPT4B,
                api_base=OLLAMA_LOCAL_HOST,
                custom_llm_provider="ollama",
                flatten_messages_as_text=True,
            )
        case ModelName.OLLAMA_LLAMA3:
            return LiteLLMModel(
                model_id=ModelName.OLLAMA_LLAMA3,
                api_base=OLLAMA_LOCAL_HOST,
                custom_llm_provider="ollama",
                flatten_messages_as_text=True,
            )
        case ModelName.GOOGLE_GEMINI_15_FLASH:
            return LiteLLMModel(
                model_id="gemini/gemini-1.5-flash", 
                api_key=GEMINI_API_KEY,
                provider="google",  
                drop_params=True,  
                **{
                    "temperature": 0.7,
                    "top_p": 0.9
                }
            )
        case ModelName.GOOGLE_GEMINI_20_FLASH:
            return LiteLLMModel(
                model_id="gemini/gemini-2.0-flash-exp", 
                api_key=GEMINI_API_KEY,
                provider="google",  
                # drop_params=True,  
                # **{
                #     "temperature": 0.7,
                #     "top_p": 0.9
                # }
            )
        case ModelName.GOOGLE_GEMINI_20_PRO:
            return LiteLLMModel(
                model_id="gemini/gemini-2.0-pro", 
                api_key=GEMINI_API_KEY,
                provider="google",  
                # drop_params=True,  
                # **{
                #     "temperature": 0.7,
                #     "top_p": 0.9
                # }
            )
        case ModelName.GOOGLE_GEMINI_25_FLASH:
            return LiteLLMModel(
                model_id="gemini/gemini-2.5-flash", 
                api_key=GEMINI_API_KEY,
                provider="google",  
                # drop_params=True,  
                # **{
                #     "temperature": 0.7,
                #     "top_p": 0.9
                # }
            )
        case ModelName.GOOGLE_GEMINI_25_PRO:
            return LiteLLMModel(
                model_id="gemini/gemini-2.5-pro", 
                api_key=GEMINI_API_KEY,
                provider="google",  
                # drop_params=True,  
                # **{
                #     "temperature": 0.7,
                #     "top_p": 0.9
                # }
            )
        case _:
            raise ValueError(f"Model {model_name} is not supported")
