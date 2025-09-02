import requests

def test_get_user_by_id():
    base_url = 'https:jsonplaceholder.typicode.com'
    user_id = 1
    response = requests.get(f"{base_url}/users{user_id}")
    assert response.status_code == 200
    user_date = response.json()
    assert user_date['id'] == user_id
    assert user_date['name'] == "Leanne Graham"
    assert isinstance(user_date['email'],str)