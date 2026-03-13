from langchain_community.utilities import SQLDatabase
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
from urllib.parse import quote_plus

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

host = "localhost"
port = "3306"
username = "root"
password = quote_plus("Aviral@2316")
database_schema = "text_to_sql"

mysql_uri = f"mysql+pymysql://{username}:{password}@{host}:{port}/{database_schema}"

db = SQLDatabase.from_uri(mysql_uri, sample_rows_in_table_info=1)


def get_schema(_):
    return db.get_table_info()


template = """
Based on the table schema below write a SQL query that answers the user question.

Only return SQL query.
Do not add explanation.
Single line query only.

Schema:
{schema}

Question:
{question}

SQL Query:
"""

prompt = ChatPromptTemplate.from_template(template)

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    api_key=api_key
)

sql_chain = (
    RunnablePassthrough.assign(schema=get_schema)
    | prompt
    | llm
    | StrOutputParser()
)


def generate_sql_query(question):
    response = sql_chain.invoke({"question": question})
    return response.strip()