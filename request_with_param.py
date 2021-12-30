import requests


parameter = {"name": "Alex"}
response = requests.get("https://playground.learnqa.ru/api/hello", params=parameter)
print(response.text)
