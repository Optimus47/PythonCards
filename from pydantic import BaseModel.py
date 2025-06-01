from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

user = User(name="Анна", age=30)
print(user.model_dump())  # {'name': 'Анна', 'age': 30}

from pydantic import ValidationError

try:
    User(name="Аня", age="не число")
except ValidationError as e:
    print(e)
