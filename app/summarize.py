from ollama import Client

class Summarizer:
    
    def __init__(self):
        self.client = Client()

    def summarize_text(self, text, model="gemma3:1b"):
        prompt = f"Summarize the following text:\n{text}"
        response = self.client.chat(model=model, messages=[{'role': 'user', 'content': prompt}])
        return response['message']['content']

# text_to_summarize = """
# Large language models (LLMs) are transforming various industries with their advanced natural language processing capabilities. 
# These models, trained on massive datasets, can generate human-quality text, translate languages, and answer questions in an informative way. 
# However, deploying and managing LLMs can be challenging, requiring significant computational resources and expertise. 
# Ollama simplifies this process by providing a framework to run LLMs locally.
# """

# summary = summarize_text(text_to_summarize)
# print(summary)