from langchain.chat_models import init_chat_model

# llm = init_chat_model("gemini-2.5-flash", model_provider="google_genai")
llm = init_chat_model("groq:openai/gpt-oss-20b")