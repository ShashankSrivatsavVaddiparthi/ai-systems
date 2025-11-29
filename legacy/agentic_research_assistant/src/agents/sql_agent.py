from langgraph.prebuilt import create_react_agent
from utils.llm import llm
from tools.sql_tools import sql_tools
from utils.prompts import sql_agent_prompt

sql_agent = create_react_agent(
    model=llm,
    tools=sql_tools,
    prompt=sql_agent_prompt,
    name="SQLAgent",
)