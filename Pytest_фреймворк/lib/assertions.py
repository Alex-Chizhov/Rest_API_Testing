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
