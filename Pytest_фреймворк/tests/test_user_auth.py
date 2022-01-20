import pytest
from ..lib.mod_requests import ModRequests
from ..lib.base_case import BaseCase
from ..lib.assertions import Asserions

class TestUserAuth(BaseCase):

    exclude_params = ["no_cookie", "no_token"]

    def setup(self):

        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'}

        response1 = ModRequests.post('/user/login', data=data)

        self.auth_sid = self.get_cookie(response1, "auth_sid")
        self.token = self.get_header(response1, "x-csrf-token")
        self.user_id_from_login_method = self.get_json_value(response1, "user_id")


    def test_auth_user(self):

        response2 = ModRequests.get("/user/auth",
                                 headers={"x-csrf-token": self.token},
                                 cookies={"auth_sid": self.auth_sid}
                                 )

        Asserions.assert_json_value_by_name(
            response2,
            key_name="user_id",
            expected_value=self.user_id_from_login_method,
            error_message="User id from auth method is not equal user id from login method"
        )

    @pytest.mark.parametrize("condition", exclude_params)
    def test_negative_auth_user(self, condition):

        if condition == "no_cookie":
            response2 = ModRequests.get("/user/auth",
                                     headers={"x-csrf-token": self.token})
        else:
            response2 = ModRequests.get("/user/auth",
                                     cookies={"auth_sid": self.auth_sid})

        Asserions.assert_json_value_by_name(
            response2,
            key_name="user_id",
            expected_value=0,
            error_message=f"User is authorized with data only: {condition}"
        )
