import requests
from endpoints.json_scheme import CreateScheme
from bs4 import BeautifulSoup
from endpoints.base_endpoint import BaseEndpoint
from tests.settings import BASE_URL, PAYLOAD


class CreateMeme(BaseEndpoint):

    def create_publication_meme(self, token, payload=None):
        payload = payload if payload else PAYLOAD
        headers = {
            'Authorization': f'{token}'
        }
        self.response = requests.post(f'{BASE_URL}/meme', headers=headers, json=payload)
        self.status_code = self.response.status_code
        self.response_json = self.response.json()
        self.response_data = CreateScheme(**self.response.json())

    def delete_publication_meme(self, token):
        headers = {
            'Authorization': f'{token}'
        }
        self.response_data = CreateScheme(**self.response.json())
        post_id = self.response_data.id
        self.response = requests.delete(f'{BASE_URL}/meme/{post_id}', headers=headers)

    def check_response_text(self, expected_text):
        assert self.response_data.text == expected_text, f"Expected text '{expected_text}' not found in response"

    def create_publication_without_authorization(self, wrong_token, payload=None):
        payload = payload if payload else PAYLOAD
        headers = {
            'Authorization': f'{wrong_token}'
        }
        self.response = requests.post(f'{BASE_URL}/meme', headers=headers, json=payload)
        soup = BeautifulSoup(self.response.text, 'html.parser')
        title_tag = soup.find('title')
        assert title_tag.text == "401 Unauthorized",\
            f"Expected title to be '401 Unauthorized' but got '{title_tag.text}'"

    def check_create_without_url(self, token):
        payload = {
            "text": "Vintage Pepe Meme Poster",
            "tags": ["meme", "vintage", "pepe", "poster"],
            "info": {}
        }
        headers = {'Authorization': f'{token}'}
        self.response = requests.post(f'{BASE_URL}/meme', headers=headers, json=payload)
        soup = BeautifulSoup(self.response.text, 'html.parser')
        p_tag = soup.find('p')
        assert p_tag.text == "Invalid parameters", f"Invalid parameters but got '{p_tag.text}'"

    def check_len_text_in_payload(self, token):
        payload = {
            "text": "Vintage" * 1000000,
            "url": "https://www.europosters.eu/marketplace/vintage-pepe-meme-v129122",
            "tags": ["meme", "vintage", "pepe", "poster"],
            "info": {}
        }
        headers = {'Authorization': f'{token}'}
        self.response = requests.post(f'{BASE_URL}/meme', headers=headers, json=payload)






