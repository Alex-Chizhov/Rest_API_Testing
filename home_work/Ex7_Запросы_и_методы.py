"""
Сегодня задача должна быть попроще. У нас есть вот такой URL: https://playground.learnqa.ru/ajax/api/compare_query_type
Запрашивать его можно четырьмя разными HTTP-методами: POST, GET, PUT, DELETE

При этом в запросе должен быть параметр method. Он должен содержать указание метода, с помощью которого вы делаете запрос.
Например, если вы делаете GET-запрос, параметр method должен равняться строке ‘GET’.
Если POST-запросом - то параметр method должен равняться ‘POST’. И так далее.

Надо написать скрипт, который делает следующее:

1. Делает http-запрос любого типа без параметра method, описать что будет выводиться в этом случае.
2. Делает http-запрос не из списка. Например, HEAD. Описать что будет выводиться в этом случае.
3. Делает запрос с правильным значением method. Описать что будет выводиться в этом случае.
4. С помощью цикла проверяет все возможные сочетания реальных типов запроса и значений параметра method.
Например с GET-запросом передает значения параметра method равное ‘GET’, затем ‘POST’, ‘PUT’, ‘DELETE’ и так далее.
И так для всех типов запроса. Найти такое сочетание, когда реальный тип запроса не совпадает со значением параметра,
но сервер отвечает так, словно все ок. Или же наоборот, когда типы совпадают, но сервер считает, что это не так.

Не забывайте, что для GET-запроса данные надо передавать через params=
А для всех остальных через data=
"""
import requests

# 1
response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type")
print(response.status_code, response.text)  # 200 Wrong method provided

# 2
response2 = requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method": "HEAD"})
print(response2.status_code, response2.text)    # 400

# 3
response3 = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method": "PUT"})
print(response3.status_code, response3.text)    # 200 {"success":"!"}

# 4
request_types = [requests.get, requests.put, requests.post, requests.delete]
parameters = ["POST", "GET", "PUT", "DELETE"]

for request_type in request_types:
    for parameter in parameters:
        if request_type == requests.get:
            response = request_type("https://playground.learnqa.ru/ajax/api/compare_query_type", params={"method": f"{parameter}"})
        else:
            response = request_type("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method": f"{parameter}"})

        if request_type.__name__ == parameter.lower() and response.text != '{"success":"!"}' or request_type.__name__ != parameter.lower() and response.text == '{"success":"!"}':
            print(request_type.__name__,  parameter.lower(), response.text) # delete get {"success":"!"}