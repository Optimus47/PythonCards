import argparse

parser = argparse.ArgumentParser(description="Пример скрипта")
parser.add_argument("name", help="Имя пользователя")
parser.add_argument("--age", type=int, help="Возраст", default=18)

args = parser.parse_args()

print(f"Привет, {args.name}! Тебе {args.age} лет.")
