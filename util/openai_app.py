# openai_app.py
import openai

class OpenAIApp:
    def __init__(self, api_key):
        openai.api_key = api_key

    def get_response(self, prompt, chat_history):
        context = "\n".join(chat_history[-5:])  
        full_prompt = f"{context}\nYou: {prompt}\nGPT:"
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4-1106-preview",
                messages=[{"role": "user", "content": full_prompt}]
            )
            # type: ignore
            return response.choices[0].message.content
        except Exception as e:
            raise e


