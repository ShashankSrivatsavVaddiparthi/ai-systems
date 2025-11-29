# Imports
import os
import wave
from piper import PiperVoice
from dotenv import load_dotenv

load_dotenv()

PIPER_MODEL_PATH = os.getenv("PIPER_MODEL_PATH")
PIPER_CONFIG_PATH = os.getenv("PIPER_CONFIG_PATH")
voice = PiperVoice.load(PIPER_MODEL_PATH, config_path=PIPER_CONFIG_PATH)

def synthesize_audio(text: str, ts: str) -> str:
    """synthesizes audio from text using Piper and saves it."""
    # audio_bytes = voice.synthesize(text)
    # return audio_bytes
    output_dir = "data/output/audio"
    os.makedirs(output_dir, exist_ok=True)
    file_path = f"{output_dir}/{ts}.wav"
    with wave.open(file_path, "wb") as wav_file:
        voice.synthesize_wav(text, wav_file)

    return file_path