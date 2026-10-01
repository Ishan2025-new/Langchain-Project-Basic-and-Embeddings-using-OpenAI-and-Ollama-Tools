import os
from langchain_openai import ChatOpenAI
import streamlit as st
from langchain_core.globals import set_debug

set_debug(True)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
llm=ChatOpenAI(model="gpt-5-mini", api_key=OPENAI_API_KEY)

st.title("Ask Anything")

question = st.text_input("Enter the question:")

if question:
    response = llm.invoke(question)
    st.write(response.content)