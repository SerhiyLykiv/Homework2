#Завдання 1
import random
numer = []
count = 0
while count < 10:
    numer = random.randint(1, 100) 
    numer.append(numer)
    count += 1
maxnumer = numer[0]
for numer in numer:
    if numer > maxnumer:
        maxnumer = numer
print("Список чисел:", numer)
print("Найбільше число:", maxnumer)

#Завдання 2
import random
list1 = []
list2 = []
count = 0
while count < 10:
    numer = random.randint(1, 10)  
    list1.append(numer)
    count += 1
count = 0
while count < 10:
    numer = random.randint(1, 10)  
    list2.append(numer)
    count += 1
cmon_numer = []
for numer in list1:
    if numer in list2 and numer not in cmon_numer:
        cmon_numer.append(numer)
print("Перший список:", list1)
print("Другий список:", list2)
print("Спільні числа (без повторень):", cmon_numer)

#Завдання3
numer1 = []
i = 1
while i <= 100:
    numer1.append(i)
    i += 1
resultat = []
i = 0
while i < len(numer1):
    num = numer1[i]
    if num % 7 == 0 and num % 5 != 0:
        resultat.append(num)
    i += 1
print("Числа, які діляться на 7, але не кратні 5:", resultat)