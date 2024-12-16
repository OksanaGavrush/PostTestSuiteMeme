import requests
from endpoints.base_endpoint import BaseEndpoint


class GetMeme(BaseEndpoint):
    def get_meme_without_authorize(self, post_id):
        self.response = requests.get(f'http://167.172.172.115:52355/meme/{post_id}')

    def get_meme_with_not_valid_id(self, token, post_id):
        headers = {
            'Authorization': f'{token}'
        }
        self.response = requests.get(f'http://167.172.172.115:52355/meme{post_id}', headers=headers)

    def get_meme_by_id(self, token, post_id):
        headers = {
            'Authorization': f'{token}'
        }
        self.response = requests.get(f'http://167.172.172.115:52355/meme/{post_id}', headers=headers)
        print(self.response.status_code)
        print(self.response.text)

    def get_oll_list_memes(self, token):
        headers = {
            'Authorization': f'{token}'
        }
        self.response = requests.get(f'http://167.172.172.115:52355/meme', headers=headers)
        print(self.response.text)

    def get_meme_with_invalid_id(self, token, post_id):
        headers = {
            'Authorization': f'{token}'
        }
        self.response = requests.get(f'http://167.172.172.115:52355/meme/{post_id}', headers=headers)
