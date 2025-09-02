import requests

url= "https://jsonplaceholder.typicode.com/users/1"
post_url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)
dict_1={"name":"Taran",
      "email":"123@qq.com",
      "address":"china"}

if __name__ == '__main__':
    print(response)
    status_code = response.status_code
    print(status_code)
    assert status_code == 200

    json_date =response.json()
    assert json_date['id'] == 1
    print('AA')
    assert isinstance(json_date['name'],str)
    print('bb')
    assert isinstance(json_date['email'],str)
    print('CC')
    try:
        json_date = response.json()
        print(json_date)
    except Exception as e:
        print(f"内容解析失败")

    post_response = requests.post(post_url,json=dict_1)
    post_json = post_response.json()
    print(f"状态码：{post_response.status_code}")
    print(f"{post_json}")
    assert post_response == 201
    print(f"请求成功")