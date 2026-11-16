from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
import tools

load_dotenv()

model = init_chat_model("openai:gpt-5-mini")
agent = create_agent(
	model,
	[tools.list_tables,
	tools.describe_table,
	tools.run_query],
	system_prompt="You answer questions about a trading database. Use the tools to look at the tables, write SQL, and base your answer only on the query results."
	)

