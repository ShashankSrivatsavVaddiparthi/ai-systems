import gradio as gr
from src.stt import transcribe_audio, save_transcript
from src.llm import run_llm, save_llm_output
from src.tts import synthesize_audio
from src.utils.time_utils import timestamp

def pipeline(audio_file):
    if audio_file is None:
        return "", None

    # audio_file is a real WAV file produced by Gradio
    #Timestamp
    ts = timestamp()

    # 1. STT
    transcript = transcribe_audio(audio_file)
    _ = save_transcript(transcript, ts)

    # 2. LLM
    llm_output = run_llm(transcript)
    _ = save_llm_output(llm_output, ts)

    # 3. TTS
    out_path = synthesize_audio(llm_output, ts)

    # out_path is something like data/output/audio/20251121_050422.wav
    return llm_output, out_path


with gr.Blocks() as app:
    gr.Markdown("### Voice Chat — STT → LLM → TTS")

    mic = gr.Audio(
        sources=["microphone"],
        type="filepath",
        label="Record"
    )

    output_text = gr.Textbox(label="LLM Output")
    output_audio = gr.Audio(label="Reply Audio", autoplay=True)

    # When STOP is pressed, run pipeline
    mic.stop_recording(
        fn=pipeline,
        inputs=mic,
        outputs=[output_text, output_audio]
    )

app.launch()
