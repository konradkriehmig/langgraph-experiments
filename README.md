# langgraph-experiments

A ReAct agent answers questions about a Postgres trading database by writing SQL. A verifier checks each answer against the query results and retries if it's unsupported.

Stack: LangGraph, LangChain, PostgreSQL on k3s, Azure AI Foundry.
