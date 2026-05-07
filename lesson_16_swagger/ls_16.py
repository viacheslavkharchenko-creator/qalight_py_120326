
import requests
import os
from dotenv import load_dotenv

load_dotenv()


def get_method(url:str = "https://www.example.com", params:dict={}):
    """ Getting data... """
    response = requests.get(url, params=params)
    return response


def post_method(url:str = "https://www.example.com", data_to_send:dict = {}, xform=False):
    """ Getting data... """
    if xform:
        response = requests.post(url, data=data_to_send)
    else:
        response = requests.post(url, json=data_to_send)
    return response


def put_method(url:str = "https://www.example.com", data_to_send:dict = {}):
    """ Getting data... """
    response = requests.put(url, json=data_to_send)
    return response

def auth_signin(username:str, password:str, headers={}):
    endpoint = "/api/auth/signin/"
    base_url = "http://localhost:8000"
    test_url = base_url + endpoint
    data = {
        "username": username,
        "password": password 
    }
    resp = post_method(test_url, data)
    return resp

if __name__ == "__main__":
    uname = os.getenv("FL_USERNAME")
    paswd = os.getenv("PASSWORD")
    print(uname, paswd)
    r = auth_signin(uname, paswd)
    print(r.request.body)
    print(r.json())