from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv
from src.routers import transcribe_router, inference_router, synthesize_router, chat_router

load_dotenv()

app = FastAPI(title="Voice Assistant (MVP)")

@app.get("/")
def root():
    return {"status": "ok"}

app.include_router(transcribe_router)
app.include_router(inference_router)
app.include_router(synthesize_router)
app.include_router(chat_router)

app.mount("/audio", StaticFiles(directory="data/output/audio"), name="audio")