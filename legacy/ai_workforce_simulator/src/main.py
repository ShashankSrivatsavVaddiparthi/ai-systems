from dotenv import load_dotenv
load_dotenv()
from agents.agents import supervisor
from utils.message_display import pretty_print_messages, pretty_print_message
from langchain_core.messages import convert_to_messages


payload = {
    "messages": [
        {
            "role": "user",
            "content": (
                "Create a simple Python script that prints 'Hello, World!' to the console. "
            ),
        }
    ]
}

print("Starting supervisor stream (showing final message per node)...")

for chunk in supervisor.stream(payload):
    pretty_print_messages(chunk, last_message=True)
    # print(chunk)

# After streaming finishes, print the final supervisor message history (if available)
try:
    final_message_history = chunk["supervisor"]["messages"]
    print("\nFinal supervisor message history:")
    for m in convert_to_messages(final_message_history):
        pretty_print_message(m)
except Exception as e:
    print("No final supervisor message history found in the last chunk:", e)