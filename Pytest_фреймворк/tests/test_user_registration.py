import requests
from ..lib.base_case import BaseCase
from ..lib.assertions import Asserions

class TestUserRegistration(BaseCase):

    def test_negative_create_user_with_existing_email(self):

        email = "vinkotov@example.com"
        data = {
            "password": "123",
            "username": "learnqa",
            "firstName": "learnqa",
            "lastName": "learnqa",
            "email": email
        }

        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)
        assert response.status_code == 400, f"Unexpected status code {response.status_code}"
        assert response.text == f"Users with email '{email}' already exists", f"Unexpected response text {response.text}"
