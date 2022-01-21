from datetime import datetime
import os
from requests import Response
import pathlib

class Logger:

    file_name = f"log_" + str(datetime.now().strftime("%Y-%m-%d_%H-%M-%S")) + ".log"
    full_path_to_log_file = pathlib.Path.cwd().parent / 'logs' / file_name

    @classmethod
    def _write_log_to_file(cls, data: str):
        with open(cls.full_path_to_log_file, "a", encoding="utf-8") as log_file:
            log_file.write(data)

    @classmethod
    def add_request(cls, url, data, headers, cookies, method):
        test_name = os.environ.get("PYTEST_CURRENT_TEST")
        # Пример:
        # test_get_user_info.py::TestUserGetInfo::test_get_user_info_not_auth (call)
        # текущий этап, может быть: setup, call, или teardown.

        data_to_add = f"""
-----
Test: {test_name}
Time: {str(datetime.now())}
Request method: {method}
Request URL: {url}
Request data: {data}
Request headers: {headers}
Request cookies: {cookies}

"""
        cls._write_log_to_file(data_to_add)

    @classmethod
    def add_response(cls, response: Response):
        cookies_as_dict = dict(response.cookies)
        headers_as_dict = dict(response.headers)

        data_to_add = f"""
Response status code: {response.status_code}
Response text: {response.text}
Response headers: {headers_as_dict}
Response cookies: {cookies_as_dict}
-----

"""
        cls._write_log_to_file(data_to_add)
