import os
import requests
import pytest


def get_token():
    if not os.path.exists('token.txt'):
        return request_new_token()

    with open('token.txt', 'r') as file:
        token = file.read()

    validate_response = requests.get(f'http://167.172.172.115:52355/authorize/{token}')
    if validate_response.status_code == 200:
        return token
    else:
        return request_new_token()


def request_new_token():
    body = {"name": 'Jupiter'}
    response = requests.post('http://167.172.172.115:52355/authorize', json=body)
    if response.status_code == 200:
        token = response.json().get('token')
        with open('token.txt', 'w') as file:
            file.write(token)
        return token
    else:
        raise Exception("Failed to retrieve new token")


@pytest.fixture(scope="session")
def token():
    return get_token()


@pytest.fixture()
def post_id():
    token = get_token()
    headers = {'Authorization': f'{token}'}
    payload = {"text": "Test meme",
               "url": "http://example.com/meme.jpg",
               "tags": ["test"],
               "info": {}}
    response = requests.post('http://167.172.172.115:52355/meme', json=payload, headers=headers)
    post_id = response.json()['id']
    yield post_id
    requests.delete(f'http://167.172.172.115:52355/meme/{post_id}', headers=headers)





