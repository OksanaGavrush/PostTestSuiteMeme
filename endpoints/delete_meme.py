import requests
from endpoints.base_endpoint import BaseEndpoint
from tests.settings import BASE_URL


class DeleteMeme(BaseEndpoint):

    def delete_publication_create_meme(self, token, post_id):
        headers = {
            'Authorization': f'{token}'
        }
        self.response = requests.delete(f'{BASE_URL}/meme/{post_id}', headers=headers)