import os
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv(), override=True)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
llm=ChatOpenAI(model="gpt-5-mini", api_key=OPENAI_API_KEY)

question = input("Enter the question: ")
response = llm.invoke(question)
print(response.content)