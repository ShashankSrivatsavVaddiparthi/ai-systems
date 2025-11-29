# Imports
import os
from fastapi import APIRouter, UploadFile, File
from fastapi import Request
from fastapi.responses import StreamingResponse
from src.stt import transcribe_audio, save_transcript
from src.llm import run_llm, stream_llm, save_llm_output
from src.tts import synthesize_audio
from src.utils.time_utils import timestamp

transcribe_router = APIRouter(tags=["Transcribe"])
inference_router = APIRouter(tags=["Inference"])
synthesize_router = APIRouter(tags=["Synthesize"])
chat_router = APIRouter(tags=["Chat"])


@transcribe_router.post("/transcribe")
async def transcribe_endpoint(audio_file: UploadFile = File(...)):
    ts = timestamp()
    audio_dir = os.path.join("data", "input", "audio")
    os.makedirs(audio_dir, exist_ok=True)
    audio_path = os.path.join(audio_dir, f"{ts}.wav")

    with open(audio_path, "wb") as f:
        f.write(await audio_file.read())
    
    text = transcribe_audio(audio_path)
    path = save_transcript(text, ts)

    return {"timestamp": ts, "text": text, "path": path}

@inference_router.post("/inference")
async def inference_endpoint(text: str):
    ts = timestamp()
    
    response = run_llm(text)
    path = save_llm_output(response, ts)
    
    return {"timestamp": ts, "response": response, "path": path}

@inference_router.post("/inference/stream")
async def inference_stream_endpoint(text: str):
    ts = timestamp()
    def llm_generator():
        for chunk in stream_llm(text):
            yield chunk
    return StreamingResponse(llm_generator(), media_type="text/plain")

@synthesize_router.post("/synthesize")
async def synthesize_endpoint(text: str, request: Request):
    ts = timestamp()
    
    path = synthesize_audio(text, ts)
    relative_url = f"/audio/{ts}.wav"

    base = str(request.base_url).rstrip("/")
    audio_url = f"{base}{relative_url}"

    return {"timestamp": ts, "path": path, "audio_url": audio_url}

@chat_router.post("/chat")
async def chat_endpoint(request: Request, audio_file: UploadFile = File(...)):
    ts = timestamp()

    # Transcribe and save audio
    audio_dir = os.path.join("data", "input", "audio")
    os.makedirs(audio_dir, exist_ok=True)
    audio_input_path = os.path.join(audio_dir, f"{ts}.wav")

    with open(audio_input_path, "wb") as f:
        f.write(await audio_file.read())
    
    text = transcribe_audio(audio_input_path)
    transcript_path = save_transcript(text, ts)

    # Run transcribed audio through LLM
    response = run_llm(text)
    llm_output_path = save_llm_output(response, ts)

    # Synthesize audio
    audio_output_path = synthesize_audio(response, ts)

    relative_url = f"/audio/{ts}.wav"
    base = str(request.base_url).rstrip("/")
    audio_url = f"{base}{relative_url}"

    # Returns
    return {
        "timestamp": ts, 
        "audio_input_path": audio_input_path, 
        "transcript_path": transcript_path, 
        "llm_output_text_path": llm_output_path, 
        "audio_output_path": audio_output_path, 
        "audio_url": audio_url
    }