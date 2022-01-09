import json

my_string = '{"answer": "Hello, Alex"}'
my_dict = json.loads(my_string)
print(my_dict)
print(my_dict['answer'])

# проверка наличия ключа в словаре
key = "one"

if key in my_dict:
    print(my_dict[key])
else:
    print(f"Ключа {key} в словаре нет")