from langgraph.prebuilt import create_react_agent
from utils.llm import llm
from tools.retrieval_tools import retrieve
from utils.prompts import retrieval_agent_prompt

retrieval_agent = create_react_agent(
    model=llm, 
    tools=[retrieve], 
    prompt=retrieval_agent_prompt,
    name="RetrievalAgent", 
)