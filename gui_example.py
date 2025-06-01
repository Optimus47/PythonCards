# -*- coding: utf-8 -*-
import tkinter as tk

def say_hello():
    label.config(text="Привет!")

root = tk.Tk()
root.title("Пример GUI")
root.minsize(200, 100)
root.configure(bg="gray")  # Установим фон окна

label = tk.Label(root, text="Нажми кнопку", bg="white", fg="black")
label.grid(row=0, column=0, padx=10, pady=10)

button = tk.Button(root, text="Поздороваться", command=say_hello)
button.grid(row=1, column=0, padx=10, pady=10)

root.update()  # Обновляем окно
root.mainloop()
