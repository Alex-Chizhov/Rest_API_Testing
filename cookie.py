import requests

# Получаем cookie
parameters = {"login": "secret_login", "password":"secret_pass"}
response = requests.post("https://playground.learnqa.ru/api/get_auth_cookie",
                         data=parameters)
print(response.text)
print(response.status_code)
print(dict(response.cookies))


# Передаём cookie серверу
cookie_value = response.cookies.get("auth_cookie")
cookies = {"auth_cookie": cookie_value}
response2 = requests.post("https://playground.learnqa.ru/api/check_auth_cookie", cookies=cookies)
print(response2.text)   # You are authorized

