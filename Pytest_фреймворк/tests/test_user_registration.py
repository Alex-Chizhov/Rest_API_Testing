import requests
from ..lib.base_case import BaseCase
from ..lib.assertions import Asserions
from datetime import datetime

class TestUserRegistration(BaseCase):

    def setup(self):
        base_part = 'email'
        domain = 'example.com'
        random_part = datetime.now().strftime("%m%d%Y%H%M%S")
        self.email = f"{base_part}{random_part}@{domain}"

    def test_create_user(self):
        data = {
            "password": "123",
            "username": "learnqa",
            "firstName": "learnqa",
            "lastName": "learnqa",
            "email": self.email
        }
        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)
        Asserions.assert_code_status(response, 200)
        Asserions.assert_json_has_key(response, "id")


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
        Asserions.assert_code_status(response, 400)
        assert response.text == f"Users with email '{email}' already exists", f"Unexpected response text {response.text}"
