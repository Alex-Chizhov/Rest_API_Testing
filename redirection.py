# при редиректе будет возвращён статус код с последнего адреса
# если передать allow_redirects=False, то редирект не будет выполнен и вернется статус код 301 с первого адреса
import requests

response = requests.post("https://playground.learnqa.ru/api/get_301", allow_redirects=True)

first_url_response = response.history[0].url
second_url_response = response.url

print(first_url_response)   # https://playground.learnqa.ru/api/get_301
print(second_url_response)  # https://www.learnqa.ru/