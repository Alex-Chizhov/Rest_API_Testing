import requests

response = requests.get("https://playground.learnqa.ru/api/hello?name=Alex")
print(response.text) # {"answer":"Hello, someone"}