import requests
from json.decoder import JSONDecodeError


response = requests.get("https://playground.learnqa.ru/api/get_text")
# проверяем является ли ответ json и ловим исключение
try:
    parsed_response_text = response.json()
    print(parsed_response_text)
except JSONDecodeError:
    print("Response is not a JSON format")