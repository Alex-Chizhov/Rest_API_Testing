# Только в GET зпаросы параметры передаються через params
# Во всех остальных звпросах параметры пережаются через data
import requests

response = requests.post("https://playground.learnqa.ru/api/check_type", data={"param1": "value1"})
print(response.text)
