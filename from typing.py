from typing import List, Dict, Optional, Union, Callable

def greet_all(names: List[str]) -> None:
    for name in names:
        print(f"Привет, {name}")

def get_value(data: Dict[str, int], key: str) -> Optional[int]:
    return data.get(key)

def handle(x: Union[int, str]) -> str:
    return str(x)

greet_all(["Alice", "Bob", "Charlie"])  # Привет, Alice