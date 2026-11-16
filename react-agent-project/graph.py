from typing import TypedDict
import agent
from langgraph.graph import StateGraph, START, END

# notepad
class State(TypedDict):
	question: str
	answer: str
	sql_result: str

# retrieve
def retrieve(state):
	result = agent.agent.invoke({"messages": [("user", state["question"])]})
	tool_results = [m.content for m in result["messages"] if m.type == "tool"]
	return {"answer": result["messages"][-1].content, "sql_result": "\n".join(tool_results)}

# verify
def verify(state):
	reply = agent.model.invoke(
		f"SQL result: {state['sql_result']} Answer: {state['answer']} "
		"Is every claim in the answer supported by the SQL result? Reply only OK or FAIL").content
	print("ANSWER:", state["answer"])
	print("VERDICT:", reply)
	if reply.startswith("OK"):
		return END
	return "retrieve"

# graph together
g = StateGraph(State)
g.add_node("retrieve", retrieve)
g.add_edge(START, "retrieve")
g.add_conditional_edges("retrieve", verify)
app = g.compile().with_config({"recursion_limit": 10})
