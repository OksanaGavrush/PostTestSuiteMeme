import pytest
import requests
from endpoints.create_meme import CreateMeme
from endpoints.get_meme import GetMeme
from endpoints.put_meme import PutMeme
from endpoints.delete_meme import DeleteMeme


@pytest.mark.auth
@pytest.mark.create
def test_create_pub(token):
    create_meme = CreateMeme()
    create_meme.create_publication_meme(token)
    create_meme.check_response_status_code_is_200()
    create_meme.check_response_text('Vintage Pepe Meme Poster')
    create_meme.delete_publication_meme(token)
    create_meme.check_response_status_code_is_200()


@pytest.mark.auth
@pytest.mark.error_handling
def test_create_post_without_authorization():
    create_meme = CreateMeme()
    create_meme.create_publication_without_authorization('wrong_token')
    create_meme.check_response_status_code_is_401()


@pytest.mark.create
@pytest.mark.error_handling
def test_create_post_without_url(token):
    create_meme = CreateMeme()
    create_meme.check_create_without_url(token)
    create_meme.check_response_status_code_is_400()


@pytest.mark.create
@pytest.mark.validation
def test_check_max_len_text(token):
    create_meme = CreateMeme()
    create_meme.check_len_text_in_payload(token)
    create_meme.check_response_status_code_is_200()
    create_meme.delete_publication_meme(token)


@pytest.mark.auth
@pytest.mark.error_handling
def test_meme_not_authorize(post_id):
    get_meme = GetMeme()
    get_meme.get_meme_without_authorize(post_id)
    get_meme.check_response_status_code_is_401()


@pytest.mark.read
def test_get_meme(token, post_id):
    get_meme = GetMeme()
    get_meme.get_meme_by_id(token, post_id)
    get_meme.check_response_status_code_is_200()


@pytest.mark.read
def test_get_oll_meme(token, post_id):
    get_meme = GetMeme()
    get_meme.get_oll_list_memes(token)
    get_meme.check_response_status_code_is_200()


@pytest.mark.error_handling
def test_get_meme_invalid_id(token, post_id):
    get_meme = GetMeme()
    get_meme.get_meme_with_not_valid_id(token, 3333)
    get_meme.check_response_status_code_is_410()


def test_replace_old_meme_with_new(token, post_id):
    put_meme = PutMeme()
    put_meme.change_meme_data(token, 95)
    put_meme.check_response_status_code_is_200()



