import requests


def post_method(url:str = "https://www.example.com", data_to_send:dict = {}, headers={}):
    """ Getting data... """
    response = requests.post(url, json=data_to_send, headers=headers)
    return response


def get_method(url:str = "https://www.example.com", data_to_send:dict = {}, headers={}):
    """ Getting data... """
    response = requests.get(url, params=data_to_send, headers=headers)
    return response


def auth_signin(username:str, password:str, headers={}):
    endpoint = "/api/auth/signin/"
    base_url = "http://127.0.0.1:8000"
    test_url = base_url + endpoint
    data = {
        "username": username,
        "password": password 
    }
    resp = post_method(test_url, data, headers=headers)
    return resp


def get_me(headers):
    endpoint = "/api/users/me/"
    base_url = "http://127.0.0.1:8000"
    test_url = base_url + endpoint

    resp = get_method(test_url, headers=headers)
    return resp


def test_positive_sigin(valid_user):
    username, password = valid_user
    resp = auth_signin(username, password)
    assert resp.status_code == 200, "Unexpect status"
    resp_json = resp.json()
    assert 'access' in resp_json and 'refresh' in resp_json, \
        "Should be exist 'access' and 'refresh' token"
    
    assert len(resp_json['access']) > 10, "Too short token value"
    assert len(resp_json['refresh']) > 10, "Too short token value"
    token = resp_json['access']
    headers = {"Authorization": f"Bearer {token}"}
    test_me = get_me(headers)
    resp_json = test_me.json()
    assert len(resp_json) >= 4, resp_json


def test_trouble_signin(valid_user):
    username, _ = valid_user
    password = "InvalidPA$$w0rd"
    resp = auth_signin(username, password)
    assert resp.status_code == 401, f"Unexpect status: {resp.text}"
    resp_json:dict = resp.json()
    assert resp_json.get('detail', "") == 'No active account found with the given credentials', \
        f"Get: {resp_json}"


if __name__ == "__main__":
    pass
