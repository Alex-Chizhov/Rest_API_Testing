"""
Необходимо написать тест, который делает запрос на метод: https://playground.learnqa.ru/api/homework_cookie
Этот метод возвращает какую-то cookie с каким-то значением.
Необходимо с помощью функции print() вывести cookie и его значение,

Чтобы pytest не игнорировал print() необходимо использовать ключик "-s": python -m pytest -s my_test.py
"""
import requests

def test_print_cookie():
    response = requests.get("https://playground.learnqa.ru/api/homework_cookie")
    #print(dict(response.cookies))   # {'HomeWork': 'hw_value'}
    assert dict(response.cookies) == {'HomeWork': 'hw_value'}, \
        f"Cookie {dict(response.cookies)} is not equal {{'HomeWork': 'hw_value'}}"

