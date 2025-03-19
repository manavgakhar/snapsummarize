from ollama import Client

class Summarizer:
    
    def __init__(self):
        self.client = Client()

    def summarize_text(self, text, model="gemma3:1b"):
        prompt = f"Summarize the following text:\n{text}"
        response = self.client.chat(model=model, messages=[{'role': 'user', 'content': prompt}])
        return response['message']['content']