from dotenv import load_dotenv
import os
load_dotenv()

from utils.helpers import get_response
from agents.assistant_agent import assistant_agent


def __main__():
    query = "Use the uploaded docs to answer 'What is Task Decomposition?'"
    response = get_response(input_text=query, agent=assistant_agent)
    print("Response:", response)
    # print("Full Response:", full_response)

__main__()