retheny = input("Введіть рядок: ")
liculnuk = 0
i = 0
while i < len(retheny) and retheny[i] == ' ':
    i += 1
while i < len(retheny):
    if retheny[i] == ' ':
        liculnuk += 1
        while i < len(retheny) and retheny[i] == ' ':
            i += 1
    else:
        i += 1
if retheny[-1] != ' ' and len(retheny) > 0:
    liculnuk += 1
print(f"Кількість слів у рядку: {liculnuk}")

#завдання 6
import random
rand2 = random.randint(1, 100)
print("Я загадав число від 1 до 100. Спробуй вгадати!")
zmina = None
while zmina != rand2:
    zmina = int(input("Введіть ваше припущення: "))
    if zmina < rand2:
        print("Забагато! Спробуйте ще раз.")
    elif zmina > rand2:
        print("Замало! Спробуйте ще раз.")
    else:
        print("Вітаємо! Ви вгадали число!")


#Завдання 7

nomer = 1
while nomer <= 10:
    print(nomer)
    nomer += 1 


#Завдання 8
Corect = "secret123"
lihilnic = 0
while lihilnic < 3:
    password = input("Введіть пароль: ")
    if password == Corect:
        print("Вітаємо! Ви ввели правильний пароль.")
        break 
    else:
        lihilnic += 1
        print(f"Невірний пароль. У вас залишилося {3 - lihilnic} спроб.")
if lihilnic == 3:
    print("Ви перевищили кількість спроб. Програма завершується.")

#Завдання 9
nuz = 10
uper = 20
while True:
    numeruzer = int(input(f"Введіть число від {nuz} до {uper}: "))
    if nuz <= numeruzer <= uper:
        print(f"Число {numeruzer} входить в діапазон.")
        break  
    else:
        print(f"Число {numeruzer} не входить в діапазон. Спробуйте знову.")

# Завдання 10 
ocinka = int(input("Введіть вашу оцінку за тест: "))
if ocinka > 90:
    print("Відмінно!")
elif 70 <= ocinka <= 90:
    print("Добре!")
else:
    print("Потрібно більше попрацювати!")

# Завдання 11
import random
randoma1 = random.randint(1, 10)
numeruzer = int(input("Введіть число від 1 до 10: "))
if numeruzer == randoma1:
    print("Вітаємо! Ви вгадали число!")
else:
    print(f"Ви програли. Ваше число: {numeruzer}, загаданое число: {randoma1}.")