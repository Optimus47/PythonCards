import pickle
import os

class Evil:
    def __reduce__(self):
        return (os.system, ("echo Вредоносный код выполнен!",))

# Сохраняем вредоносный объект
with open("evil.pkl", "wb") as f:
    pickle.dump(Evil(), f)

# При загрузке этого файла будет выполнена команда в системе!
with open("evil.pkl", "rb") as f:
    pickle.load(f)  # Опасно! Выполнит os.system(...)

data = {"name": "Анна", "age": 30}

with open("data.pkl", "wb") as f:
    pickle.dump(data, f)

with open("data.pkl", "rb") as f:
    loaded_data = pickle.load(f)

print(loaded_data)
# Output: {'name': 'Анна', 'age': 30'}

a: list[int] = [1, 2, 3]
b: dict = {"x": 10, "y": 20}
print(__annotations__)


with open("multi.pkl", "wb") as f:
    pickle.dump(a, f)
    pickle.dump(b, f)

with open("multi.pkl", "rb") as f:
    a_loaded = pickle.load(f)
    b_loaded = pickle.load(f)

print(a_loaded)  # [1, 2, 3]
print(b_loaded)  # {'x': 10, 'y': 20}