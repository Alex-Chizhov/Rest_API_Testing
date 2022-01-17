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
    def assert_json_has_keys(response: Response, key_list: list):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is {response.text}"

        for key in key_list:
            assert key in response_as_dict, f"Response JSON doesn't have key '{key}'"

    @staticmethod
    def assert_code_status(response: Response, expected_status_code):
        assert response.status_code == expected_status_code, \
            f"Unexpected status code: {response.status_code}. Expected status code : {expected_status_code}"

    @staticmethod
    def assert_json_has_no_key(response: Response, key_name):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is {response.text}"

        assert key_name not in response_as_dict, f"Response JSON have key '{key_name}'"

    @staticmethod
    def assert_json_has_no_keys(response: Response, key_list: list):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is {response.text}"

        for key in key_list:
            assert key not in response_as_dict, f"Response JSON have key '{key}'"