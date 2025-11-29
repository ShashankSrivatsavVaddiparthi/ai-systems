from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
load_dotenv()

# reasoning_llm = init_chat_model("gemini-2.5-pro", model_provider="google_genai")
reasoning_llm = init_chat_model("groq:openai/gpt-oss-20b")