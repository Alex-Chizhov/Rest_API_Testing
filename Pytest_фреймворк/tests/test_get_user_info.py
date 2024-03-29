from ..lib.base_case import BaseCase
from ..lib.assertions import Asserions
from ..lib.mod_requests import ModRequests

class TestUserGetInfo(BaseCase):

    def test_get_user_info_not_auth(self):
        response = ModRequests.get("/user/2")
        Asserions.assert_json_has_key(response, "username")
        Asserions.assert_json_has_no_keys(response, ["email", "firstName", "lastName"])

    def test_login_and_get_user_info(self):
        response1 = ModRequests.post("/user/login", data={"email": "vinkotov@example.com", "password": "1234"})

        auth_sid = self.get_cookie(response1, "auth_sid")
        token = self.get_header(response1, "x-csrf-token")
        user_id_from_login_method = self.get_json_value(response1, "user_id")

        response2 = ModRequests.get(f"/user/{user_id_from_login_method}",
                                 headers={"x-csrf-token": token},
                                 cookies={"auth_sid": auth_sid}
                                 )

        Asserions.assert_json_has_keys(response2, ["username", "email", "firstName", "lastName"])
