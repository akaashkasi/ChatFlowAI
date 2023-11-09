# chat_app.py
import streamlit as st
import uuid

class ChatApp:
    def __init__(self, ai_app):
        self.ai_app = ai_app
        self.chat_placeholder = st.empty()

    def update_chat_history(self, role, message):
        if 'chat_history' not in st.session_state:
            st.session_state['chat_history'] = []
        st.session_state['chat_history'].append(f"{role}: {message}")
        self.display_chat_history()

    def display_chat_history(self):
        chat_history = st.session_state.get('chat_history', [])
        chat_text = '\n'.join(chat_history)
        unique_key = f"chat_text_area_{uuid.uuid4()}"
        self.chat_placeholder.text_area("Chat", chat_text, height=300, key=unique_key)

    def display(self):
        user_input = st.text_input("You:", key='user_input')
        if st.button("Send"):
            self.update_chat_history("You", user_input)
            # Pass the entire chat history for context when generating the response
            chat_history = st.session_state.get('chat_history', [])
            gpt_response = self.ai_app.get_response(user_input, chat_history)
            if gpt_response:
                self.update_chat_history("GPT", gpt_response)
