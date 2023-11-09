# openai_app.py
import openai

class OpenAIApp:
    def __init__(self, api_key):
        openai.api_key = api_key

    def get_response(self, prompt):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4-1106-preview",
                messages=[{"role": "user", "content": prompt}]
            )
            # The following line assumes that the response object has a key 'choices'
            # which is a list, and each choice has a 'message' key which in turn contains 'content'.
            # You will need to verify this against the actual API documentation or response.
            return response.choices[0].message.content
        except Exception as e:
            raise e


