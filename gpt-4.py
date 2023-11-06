import os
import openai
import streamlit as st

class OpenAIApp:
    def __init__(self, api_key):
        openai.api_key = api_key

    def get_response(self, prompt):
        try:
            response = openai.Completion.create(
                engine="text-davinci-002",
                prompt=prompt,
                max_tokens=150,
                temperature=0.2
            )
            if 'choices' in response and response['choices']:
                return response['choices'][0]['text'].strip()
            else:
                st.write(f"Unexpected response format: {response}")
        except Exception as e:
            st.write(f"An error occurred: {e}")

def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

class ChatApp:
    def __init__(self, ai_app):
        self.ai_app = ai_app
        self.chat_placeholder = st.empty()  # Create an empty placeholder to display chat history
        if 'chat_history' not in st.session_state:
            st.session_state['chat_history'] = [] #added chat history to be able to query conversations previously 

    def update_chat_history(self, role, message):
        st.session_state['chat_history'].append(f"{role}: {message}")
        self.chat_placeholder.text(st.session_state['chat_history_text'])  # Update the placeholder with the updated chat history

    def display(self):
        # Initialize the chat history text in session state if it's not already initialized
        if 'chat_history_text' not in st.session_state:
            st.session_state['chat_history_text'] = ""

        st.markdown(
        """
        <style>
            body {
                background-color: #f4f4f4;
            }
        </style>
        """,
        unsafe_allow_html=True
        )

        if os.path.exists('css/style.css'):
            load_css('css/style.css')
        else:
            st.write("CSS file not found")

        user_input = st.text_input("You: ")

        if st.button("Send"):
            self.update_chat_history("You", user_input)
            conversation_history = '\n'.join(st.session_state['chat_history'])  # combine all chat history into one string
            prompt = f"{conversation_history}\nGPT, answer the user as best as possible:"
            gpt_response = self.ai_app.get_response(prompt)
            if gpt_response:
                self.update_chat_history("GPT", gpt_response)
                self.display_chat_history()  # update displayed chat history
    # Displayed Chat History
    def display_chat_history(self):
        chat_text = '\n'.join(st.session_state['chat_history'])
        st.session_state['chat_history_text'] = chat_text
        self.chat_placeholder.text(chat_text)

if __name__ == "__main__":
    api_key = os.getenv("OPENAI_API_KEY")
    ai_app = OpenAIApp(api_key)
    chat_app = ChatApp(ai_app)
    chat_app.display()
