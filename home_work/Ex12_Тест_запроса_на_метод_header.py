"""
Необходимо написать тест, который делает запрос на метод: https://playground.learnqa.ru/api/homework_header
Этот метод возвращает headers с каким-то значением.
Необходимо с помощью функции print() понять что за headers и с каким значением,
и зафиксировать это поведение с помощью assert

Чтобы pytest не игнорировал print() необходимо использовать ключик "-s": python -m pytest -s my_test.py
"""
import requests

def test_print_cookie():
    response = requests.get("https://playground.learnqa.ru/api/homework_header")
    #print(response.headers)
    headers = {'Date': 'Sat, 15 Jan 2022 04:15:30 GMT', 'Content-Type': 'application/json', 'Content-Length': '15',
               'Connection': 'keep-alive', 'Keep-Alive': 'timeout=10', 'Server': 'Apache',
               'x-secret-homework-header': 'Some secret value', 'Cache-Control': 'max-age=0',
               'Expires': 'Sat, 15 Jan 2022 04:15:30 GMT'}

    for key in headers.keys():
        assert key in response.headers, f"Key '{key}' is not in '{response.headers}'"


