from langchain import HuggingFaceHub
import streamlit as st
import os

os.environ["HUGGINGFACEHUB_API_TOKEN"] = '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'

def get_response(question):
    llm = HuggingFaceHub(repo_id="google/flan-t5-large",
                         model_kwargs={"temperature": 0.2, "max_length": 64})
    response = llm(question)
    return response

st.set_page_config(page_title="Q&A BOT")
st.header("Langchain Application")

input_text = st.text_input("Input: ", key="input")
submit = st.button("Ask the question")

## If ask button is clicked
if submit and input_text:  # Check if the button is clicked and there's an input
    response = get_response(input_text)
    st.subheader("The Response is")
    st.write(response)
