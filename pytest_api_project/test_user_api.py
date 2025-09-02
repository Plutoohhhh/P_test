import requests
import pytest

@pytest.fixture()
def base_url():
    return "https://jsonplaceholder.typicode.com"

def test_get_user_by_id(base_url):
    user_id = 1
    response = requests.get(f"{base_url}/users/{user_id}")
    assert response.status_code == 200
    user_date = response.json()
    assert user_date['id'] == user_id
    assert user_date['name'] == "Leanne Graham"
    assert isinstance(user_date['email'],str)

def test_creat_new_post(base_url):
    playload = {"title":"my new book",
                "body":"This is for testing",
                "userID":55}
    reponse = requests.post(f"{base_url}/posts",json=playload)

    assert reponse.status_code == 201

    post_date = reponse.json()
    assert post_date['title'] == playload['title']
    assert post_date['body'] == playload['body']
    assert post_date['userID'] == playload['userID']
    assert 'id' in post_date

