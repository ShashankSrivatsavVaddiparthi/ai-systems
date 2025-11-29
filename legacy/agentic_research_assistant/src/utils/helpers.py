from IPython.display import display, Image
from agents.assistant_agent import assistant_agent


def get_response(input_text, agent=assistant_agent):
  input = {
      "messages": [
          {
              "role": "user", 
              "content": input_text, 
          }
      ]
  }
  config = {"configurable": {"thread_id": "123"}}
  resp = agent.invoke(input, config=config)
  return resp["messages"][-1].content#, resp

def agent_structure(agent):
  display(Image(agent.get_graph().draw_mermaid_png()))

# def set_api_keys():
#   import os
#   os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY
#   os.environ["TAVILY_API_KEY"] = TAVILY_API_KEY
#   os.environ["GROQ_API_KEY"] = GROQ_API_KEY