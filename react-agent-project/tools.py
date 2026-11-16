import psycopg2
from langchain_core.tools import tool

c = psycopg2.connect("postgresql://postgres:pass@pg.rag-agents:5432/trading")

@tool
def list_tables():
	""" lists all tables """
	cur = c.cursor()
	cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'")
	rows = cur.fetchall()
	cur.close()
	return str(rows)

@tool
def describe_table(name):
	""" describe table """
	cur = c.cursor()
	cur.execute("SELECT column_name, data_type FROM information_schema.columns WHERE table_name = %s", (name,))
	rows = cur.fetchall()
	cur.close()
	return str(rows)

@tool
def run_query(sql):
	""" run a sql query """
	cur = c.cursor()
	cur.execute(sql)
	rows = cur.fetchall()
	cur.close()
	return str(rows)


