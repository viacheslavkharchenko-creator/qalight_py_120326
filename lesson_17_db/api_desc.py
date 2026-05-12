import requests
from dataclasses import dataclass, field
from typing import Dict, Any


@dataclass
class Endpoint:
    """
    Endpoint definition with method, path and optional body.
    """
    method: str
    endpoint: str
    body: Dict[str, Any] = field(default_factory=dict)



@dataclass
class Auth:

    @property
    def api_auth_signin_post(self) -> Endpoint:
        method = "POST"
        endpoint = "/api/auth/signin/"
        body = {"username": "string", "password": "string"}
        return Endpoint(method, endpoint, body)


class WebCall:

    def __init__(self, api:Auth, base_url: str = "http://example.com"):
        self.method = api.method
        self.path = api.endpoint
        self.body = api.body
        self.base_url = base_url
    

    def request(self) -> requests.Response:
        response = requests.request(
            method=self.method,
            url= self.base_url + self.path,
            json=self.body
        )
        return response


if __name__ == "__main__":
    #endpoint = "/api/auth/signin/"
    base_url = "http://127.0.0.1:8000"
    #test_url = base_url + endpoint
    # data = {
    #     "username": "username",
    #     "password": "password" 
    # }
    api = Auth()
    endpoint = api.api_auth_signin_post
    call = WebCall(endpoint, base_url)
    print(call.request().json())
