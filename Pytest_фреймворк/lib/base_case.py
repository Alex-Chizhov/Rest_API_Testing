import json.decoder

from requests import Response

class BaseCase:

    #  response: Response это подсказка или аннотация (Python hint)
    #  подсказывает программисту что параметр response должен быть объектом класса Response
    def get_cookie(self, response: Response, cookie_name):
        assert cookie_name in response.cookies, f"Cannot find cookie with name {cookie_name}"
        return response.cookies[cookie_name]

    def get_header(self, response: Response, header_name):
        assert header_name in response.headers, f"Cannot find header with name {header_name}"
        return response.headers[header_name]


    def get_json_value(self, response: Response, name):
        try:
            response_as_dict = response.json()
        except json.decoder.JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is {response.text}"

        assert name in response_as_dict, f"Response JSON doesn't have key {name}"
        return response_as_dict[name]