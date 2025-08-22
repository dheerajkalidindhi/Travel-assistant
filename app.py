import streamlit as st
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

# -------------------------------
# CONFIG
# -------------------------------
st.set_page_config(page_title="🌍 Travel Assistant Chatbot", page_icon="✈️", layout="centered")

# Load environment variables
load_dotenv()

# Gemini API key (stored in .env for security)
API_KEY = os.getenv("API_KEY")

# Initialize Gemini LLM
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=API_KEY)

# Add memory to store conversation
if "memory" not in st.session_state:
    st.session_state.memory = ConversationBufferMemory(return_messages=True)

# Create conversation chain
conversation = ConversationChain(
    llm=llm,
    memory=st.session_state.memory
)

# -------------------------------
# STREAMLIT UI
# -------------------------------
st.title("✈️ Travel Assistant Chatbot")
st.write("Ask me anything about travel, flights, hotels, destinations, or tips!")

# User input
user_input = st.text_input("You:", "")

if user_input:
    response = conversation.run(user_input)
    st.write("🤖 Assistant:", response)
