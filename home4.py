# Завдання 1

import random

# Генерація випадкового числа від 1 до 10
rand = random.randint(1, 10)

# Запит користувача на вгадування числа
veden = int(input("Вгадай число від 1 до 10: "))

# Перевірка, чи вгадав користувач число
if veden == rand:
    print("Вітаємо! Ви вгадали число.")
else:
    print(f"На жаль, ви не вгадали. Правильне число було {rand}.")

# Завдання 2

 # Отримуємо ім'я користувача
name = input("Please enter your name: ")

# Отримуємо вік користувача
age = int(input("Enter your age: "))

# Виводимо привітання
print(f"Hello, {name}, on your next birthday you’ll be {age + 1} years.")

#Завдання 3

# Зчитуємо вхідний рядок
radok = input("Введіть рядок: ")

# Генеруємо і виводимо 5 випадкових рядків
for _ in range(5):
    vidpovid = ''.join(random.choice(radok) for _ in range(len(radok)))
    print(vidpovid)