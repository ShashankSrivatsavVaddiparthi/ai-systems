from dotenv import load_dotenv
import os
load_dotenv()

import gradio as gr
from utils.helpers import get_response
from agents.assistant_agent import assistant_agent



iface = gr.Interface(
    fn=get_response, 
    inputs=["text"],
    outputs=gr.Markdown(label="Response"), 
    title="Agentic Research Assistant",
    description="An AI assistant that uses multiple agents to help with research tasks.",
)

iface.launch()