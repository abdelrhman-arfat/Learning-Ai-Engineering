from .ModelService import ModelService
import requests
import os
from dotenv import load_dotenv
load_dotenv()


class JinaService(ModelService):

    def __init__(self):
        self.api_key = os.getenv("API_KEY_JINA")
        self.model_name = "jina-embeddings-v2-base-en"
        self.base_url = 'https://api.jina.ai/v1/embeddings'

    def extract_data(self, text):
        response = self.send_request(text)
        return {
            "tokens": self.extract_tokens(response),
            "embeddings": self.extract_embeddings(response)
        }

    def send_request(self, text):
        # تأكد إن input دايمًا list
        if not isinstance(text, list):
            text = [text]

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        payload = {
            "input": text,
            "model": self.model_name
        }

        response = requests.post(self.base_url, headers=headers, json=payload)

        if response.status_code != 200:
            raise Exception(
                f"API request failed: {response.status_code}, {response.text}")

        return response.json()

    def extract_embeddings(self, response):
        try:
            return [item["embedding"] for item in response["data"]]
        except KeyError:
            raise Exception("Response JSON does not contain 'data/embedding'")

    def extract_tokens(self, response):
        try:
            return response.get("usage", {}).get("total_tokens", None)
        except Exception:
            return None
