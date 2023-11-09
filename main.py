# main.py
import os
from util.openai_app import OpenAIApp
from util.chat_app import ChatApp
from misc.utils import load_css
import streamlit as st

def main():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        st.warning("Please set an environment variable 'OPENAI_API_KEY' with your OpenAI key.")
        st.stop()

    ai_app = OpenAIApp(api_key)
    chat_app = ChatApp(ai_app)

    # Load CSS
    css_file = 'css/style.css'
    if os.path.exists(css_file):
        load_css(css_file)
    else:
        st.warning("CSS file not found")

    chat_app.display()

if __name__ == "__main__":
    main()
