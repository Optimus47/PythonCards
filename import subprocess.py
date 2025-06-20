import subprocess

result = subprocess.run(["echo", "Привет!"], capture_output=True, text=True)
print(result.stdout)  # Привет!

try:
    subprocess.run(["ls", "nonexistent"], check=True)
except subprocess.CalledProcessError as e:
    print("Ошибка:", e)

# result = subprocess.run(["cat", "/etc/shadow"], capture_output=True, text=True)
# print(result.stdout)  # Вывод команды ls -l   

# Пример: автоматизация git status
git_result = subprocess.run(["git", "status"], capture_output=True, text=True)
print("Git status:\n", git_result.stdout)
