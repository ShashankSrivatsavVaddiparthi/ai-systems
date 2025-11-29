# Imports
import os
from faster_whisper import WhisperModel
from dotenv import load_dotenv

load_dotenv()

# Load whisper model for speech to text transcription
WHISPER_MODEL = os.getenv("WHISPER_MODEL", "small")
model = WhisperModel(WHISPER_MODEL, device="cpu")

# Utilizing whisper's capabilities to transcribe audio
def transcribe_audio(audio_path: str) -> str:
    """
    Takes an audio file path, runs Whisper STT, 
    and returns the transcribed text
    """
    segments, info = model.transcribe(audio_path, beam_size=5)
    full_text = " ".join([segment.text for segment in segments])
    return full_text.strip()

# Save the transcript to be sent to the LLM for inference
def save_transcript(text: str, ts: str) -> str:
    output_dir = "data/input/text"
    os.makedirs(output_dir, exist_ok=True)

    file_path = f"{output_dir}/{ts}.txt"

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(text)
    return file_path