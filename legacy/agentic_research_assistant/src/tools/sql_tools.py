from langchain_community.agent_toolkits import SQLDatabaseToolkit
from utils.sql_database import db
from utils.llm import llm

toolkit = SQLDatabaseToolkit(db=db, llm=llm)

sql_tools = toolkit.get_tools()