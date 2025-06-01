import json

# Словарь -> JSON-строка
data = {"name": "Аня", "age": 30}
json_str = json.dumps(data)
# print type of data variable
print(type(data))  # <class 'dict'>
# print type of json_str variable
print(type(json_str))  # <class 'str'>
# print JSON-строку
print(json_str)  # {"name": "Аня", "age": 30}

# JSON-строка -> словарь
parsed = json.loads(json_str)
print(parsed["name"])  # Аня

with open("data.json", "w") as f:
    json.dump(data, f)

with open("data.json", "r") as f:
    new_data = json.load(f)

print(type(new_data))  # <class 'dict'>
print(new_data)  # {'name': 'Аня', 'age': 30}