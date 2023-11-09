# openai_app.py
import openai

class OpenAIApp:
    def __init__(self, api_key):
        openai.api_key = api_key

    def get_response(self, prompt, chat_history):
        ai_introduction = (
            "This is ChatFlowAI, a conversational assistant designed to provide advice and insights. "
            "Powered by the latest GPT-4 technology, ChatFlowAI offers a dynamic and engaging conversational experience, "
            "adapting to the user's needs and retaining memory of all past interactions for contextually rich guidance. "
            "As an AI, you are to maintain a coherent conversation thread, remembering details from earlier exchanges "
            "to ensure each piece of advice or input you provide is informed by the user's history and preferences."
        )
        context = "\n".join(chat_history[-10:])  # Takes the last 10 exchanges for context
        full_prompt = f"{ai_introduction}\n{context}\nYou: {prompt}\nChatFlowAI:"
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4-1106-preview",
                messages=[{"role": "user", "content": full_prompt}]
            )
            return response.choices[0].message.content
        except Exception as e:
            raise e

