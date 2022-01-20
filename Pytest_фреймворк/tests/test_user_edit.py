from ..lib.mod_requests import ModRequests
from ..lib.base_case import BaseCase
from ..lib.assertions import Asserions

class TestUserEdit(BaseCase):

    def test_edit_user(self):
        # registration
        registration_data = self.prepare_registration_data()
        response1 = ModRequests.post("/user/",
                                  data=registration_data
                                  )
        Asserions.assert_code_status(response1, 200)
        Asserions.assert_json_has_key(response1, "id")


        email = registration_data["email"]
        password = registration_data["password"]
        user_id = self.get_json_value(response1, "id")

        # login
        login_data = {
            "email": email,
            "password": password
        }

        response2 = ModRequests.post("/user/login", data=login_data)
        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        # edit
        new_name = "New name"
        response3 = ModRequests.put(f"/user/{user_id}",
                                 headers={"x-csrf-token": token},
                                 cookies={"auth_sid": auth_sid},
                                 data={"firstName": new_name}
                                 )

        Asserions.assert_code_status(response3, 200)

        # get_user_info
        response4 = ModRequests.get(f"/user/{user_id}",
                                 headers={"x-csrf-token": token},
                                 cookies={"auth_sid": auth_sid},
                                 )

        Asserions.assert_json_value_by_name(
            response4,
            key_name="firstName",
            expected_value=new_name,
            error_message="Invalid username after editing"
        )