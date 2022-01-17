from requests import Response
import json

class Asserions:

    @staticmethod
    def assert_json_value_by_name(response: Response, key_name, expected_value, error_message):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is {response.text}"

        assert key_name in response_as_dict, f"Response JSON doesn't have key '{key_name}'"
        assert response_as_dict[key_name] == expected_value, error_message

    @staticmethod
    def assert_json_has_key(response: Response, key_name):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is {response.text}"

        assert key_name in response_as_dict, f"Response JSON doesn't have key '{key_name}'"

    @staticmethod
    def assert_code_status(response: Response, expected_status_code):
        assert response.status_code == expected_status_code, \
            f"Unexpected status code: {response.status_code}. Expected status code : {expected_status_code}"
