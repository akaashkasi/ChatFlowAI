# chat_app.py
import streamlit as st
import uuid
from css.styles import apply_styles

# Set up your Streamlit page configuration
st.set_page_config(page_title='ChatFlowAI', layout='wide', initial_sidebar_state='expanded')

# Apply custom styles from styles.py
apply_styles()

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

    def display_intro(self):
        intro_message = (
            "Hello, I'm ChatFlowAI, your conversational assistant. "
            "I'm here to provide you with conversational advice and guidance. "
            "You can ask me questions or discuss topics, and I will remember our conversations "
            "to provide consistent and contextual advice. Let's chat!"
        )
        self.update_chat_history("ChatFlowAI", intro_message)

    def display(self):
        if 'chat_initialized' not in st.session_state:
            self.display_intro()
            st.session_state['chat_initialized'] = True
        user_input = st.text_input("You:", key='user_input')
        if st.button("Send"):
            self.update_chat_history("You", user_input)
            # Pass the entire chat history for context when generating the response
            chat_history = st.session_state.get('chat_history', [])
            gpt_response = self.ai_app.get_response(user_input, chat_history)
            if gpt_response:
                self.update_chat_history("ChatFlowAI", gpt_response)
