from dotenv import load_dotenv
import streamlit as st
import os
from llama_index.llms.llama_api import LlamaAPI
from llama_index.core.llms import ChatMessage

# Load environment variables from .env file
load_dotenv()

# Set up the Llama API
api_key = os.getenv("LLAMA_API_KEY")
llm = LlamaAPI(api_key=api_key)

# Function to get response from Llama API
def get_llama_response(user_input):
    messages = [
        ChatMessage(role="system", content="You are a best code generator and provide accurate code based on user input prompt."),
        ChatMessage(role="user", content=user_input),
    ]
    resp = llm.chat(messages)
    return resp

# Initialize Streamlit app
st.set_page_config(page_title="Llama Code Generator")

st.header("CodingJr Code-Generator")

# Input text area for user prompt
user_input = st.text_area("Enter your prompt for code generation:")

# Submit button
if st.button("Generate Code with llama"):
    if user_input:
        response = get_llama_response(user_input)
        st.subheader("Generated Code:")
        st.code(response, language='python')
    else:
        st.error("Please enter a prompt.")

# Instructions to load the .env file
