import requests
from ..lib.base_case import BaseCase
from ..lib.assertions import Asserions

class TestUserRegistration(BaseCase):

    def test_create_user(self):
        data = self.prepare_registration_data()
        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)
        Asserions.assert_code_status(response, 200)
        Asserions.assert_json_has_key(response, "id")


    def test_negative_create_user_with_existing_email(self):
        email = "vinkotov@example.com"
        data = self.prepare_registration_data(email)
        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)
        Asserions.assert_code_status(response, 400)
        assert response.text == f"Users with email '{email}' already exists", f"Unexpected response text {response.text}"
