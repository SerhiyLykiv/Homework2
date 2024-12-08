#1 task
rechena = input("Введіть речення: ")
words = rechena.split()
worddikt = {}
for word in words:
    word = word.lower()
    if word in worddikt:
            worddikt[word] += 1
    else:
        worddikt[word] = 1
print(worddikt)
#2 Task
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
suma = 0
for item in stock:
    suma += stock[item] * prices.get(item, 0) 
print("Загальна ціна запасу:", suma)
#3 Task
bob = [(i, i**2) for i in range(1, 11)]
print(bob)
#4 Task
tuhden = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
daysdict = {i+1: tuhden[i] for i in range(7)}
zvorotdaysdikt = {tuhden[i]: i+1 for i in range(7)}
print("Словник (число -> день тижня):", daysdict)
print("Зворотний словник (день тижня -> число):", zvorotdaysdikt)
