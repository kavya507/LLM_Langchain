from langchain_openai import OpenAI
from dotenv import load_dotenv
import streamlit as st
import os
load_dotenv()
# function to load openAI model and get response
def get_openai_response(question):
    llm = OpenAI(openai_api_key=os.getenv("OPEN_API_KEY"), temperature = 0.3)
    response = llm.invoke(question)
    return response
    
#initialize our streamlit app
st.set_page_config(page_title="Q&A demo")
st.header("Langchain Application")
input = st.text_input("Input ", key="input")

submit = st.button("Ask the question")

#if ask is clicked
if submit:
    
    response = get_openai_response(input)
    st.subheader("The response is:")
    st.write(response)
    
