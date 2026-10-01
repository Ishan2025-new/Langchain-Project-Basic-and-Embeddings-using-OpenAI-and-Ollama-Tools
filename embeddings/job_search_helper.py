import os
from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma

from dotenv import load_dotenv,find_dotenv

load_dotenv(find_dotenv(),override=True)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
llm=OpenAIEmbeddings(api_key=OPENAI_API_KEY)


with open("job_listings.txt", "r", encoding="utf-8") as file:
    text = file.read()

document = Document(
    page_content=text,
    metadata={
        "source": "job_listings.txt"
    }
)

documents = [document]


text_splitter= RecursiveCharacterTextSplitter(chunk_size=200,
                                              chunk_overlap=10)
chunks=text_splitter.split_documents(documents)

db=Chroma.from_documents(chunks,llm)

retriever = db.as_retriever()

text = input("Enter the query: ")

docs = retriever.invoke(text)

for doc in docs:
    print(doc.page_content)