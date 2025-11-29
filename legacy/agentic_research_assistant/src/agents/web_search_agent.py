from langgraph.prebuilt import create_react_agent
from utils.llm import llm
from tools.web_search_tools import web_search
from utils.prompts import web_search_agent_prompt


web_search_agent = create_react_agent(
    model=llm,
    tools=[web_search], 
    prompt=web_search_agent_prompt,
    name="WebSearchAgent",
)