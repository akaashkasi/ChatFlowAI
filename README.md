# Simple OpenAI-Experimentation

## Added the following implementations so far:
The code initializes an interactive chat application using Streamlit for the user interface.
OpenAI's GPT-4 engine is used for generating responses to user input.
Users can type and send messages through a text input field.
Upon sending a message, the application updates the chat history with the user's message.
The application constructs a prompt based on the conversation history and sends it to GPT-4 for generating a response.
GPT-4's response is then displayed in the chat history, allowing for a back-and-forth conversation between the user and GPT-4.
The chat history is maintained across interactions using Streamlit's session state, allowing for continuous conversations.
A function is provided for loading and applying CSS styles from an external file to enhance the visual presentation of the chat interface.

### How to run:
- streamlit run {file_name}
Example:
streamlit run main.py

### Technologies used:
- Streamlit
- OpenAI GPT: "gpt-4-1106-preview"
- CSS
