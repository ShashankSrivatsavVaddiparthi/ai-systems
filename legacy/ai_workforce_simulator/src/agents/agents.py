from langchain.agents import create_agent
from langgraph_supervisor import create_supervisor
from utils.llms import reasoning_llm
from agents.agent_system_prompts import *
from tools.tools import code_tool, write_file

planner_agent = create_agent(
    model=reasoning_llm,
    tools=[],
    system_prompt=planner_agent_prompt,
    name="planner_agent",
)

developer_agent = create_agent(
    model=reasoning_llm,
    tools=[],
    system_prompt=developer_agent_prompt,
    name="developer_agent"
)

code_tester_agent = create_agent(
    model=reasoning_llm,
    tools=[code_tool],
    system_prompt=code_tester_agent_prompt,
    name="code_tester_agent"
)

code_reviewer_agent = create_agent(
    model=reasoning_llm,
    tools=[],
    system_prompt=code_reviewer_agent_prompt,
    name="code_reviewer_agent",
)

documenter_agent = create_agent(
    model=reasoning_llm,
    tools=[write_file],
    system_prompt=documenter_agent_prompt,
    name="documenter_agent",
)

supervisor = create_supervisor(
    model=reasoning_llm,
    agents=[planner_agent, developer_agent, code_tester_agent, code_reviewer_agent, documenter_agent],
    prompt=supervisor_prompt,
    add_handoff_back_messages=True,
    output_mode="full_history",
).compile()