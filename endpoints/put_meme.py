import requests
from endpoints.base_endpoint import BaseEndpoint
from tests.settings import BASE_URL


class PutMeme(BaseEndpoint):
    def change_meme_data(self, token, post_id):
        headers = {
            'Authorization': f'{token}'
        }
        payload = {
              "id": post_id,
              "text": "Meme Man - iconic surrealist meme figure",
              "url": "https://en.wikipedia.org/wiki/Meme_Man#/media/File:Meme_Man_on_transparent_background.webp",
              "tags": ["Meme Man", "surreal", "internet meme", "funny", "3D head"],
              "info": {
                "description": "Meme Man is a surreal 3D-rendered head."
              }
            }
        self.response = requests.put(f'{BASE_URL}/meme/{post_id}', headers=headers, json=payload)

