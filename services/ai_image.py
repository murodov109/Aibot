import requests

class AIImageService:
    def __init__(self, api_key):
        self.api_key = api_key
        self.api_url = "https://api.example.com/generate"

    def generate_image(self, prompt):
        response = requests.post(self.api_url, json={'prompt': prompt}, headers={'Authorization': f'Bearer {self.api_key}'})
        if response.status_code == 200:
            return response.json()['image_url']
        else:
            raise Exception(f'Error: {response.status_code}, {response.text}')