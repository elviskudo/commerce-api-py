import requests
from app.config import CHATGPT_API_KEY, CHATGPT_API_BASE_URL

class ChatGPTService:
    def __init__(self):
        self.api_key = CHATGPT_API_KEY
        self.base_url = CHATGPT_API_BASE_URL

    def get_chatgpt_response(self, prompt: str, max_tokens: int = 150, temperature: float = 0.7):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        data = {
            "model": "gpt-3.5-turbo",
            "messages": [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            "max_tokens": max_tokens,
            "temperature": temperature,
        }
        try:
            response = requests.post(
                f"{self.base_url}/chat/completions", 
                headers=headers, 
                json=data
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error communicating with ChatGPT: {e}")
            return None