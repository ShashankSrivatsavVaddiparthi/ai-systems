from langgraph_supervisor import create_supervisor
from utils.llm import llm
from agents.retrieval_agent import retrieval_agent
from agents.sql_agent import sql_agent
from agents.web_search_agent import web_search_agent
from utils.prompts import assistant_agent_prompt
from langgraph.checkpoint.memory import MemorySaver

memory = MemorySaver()
assistant_agent = create_supervisor(
    model=llm, 
    agents=[web_search_agent, retrieval_agent, sql_agent], 
    prompt=assistant_agent_prompt, 
    add_handoff_back_messages=True, 
    output_mode="full_history", 
).compile(checkpointer=memory)