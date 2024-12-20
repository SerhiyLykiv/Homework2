#task1
def oops():
    # Явно генеруємо виключення IndexError
    raise IndexError("Це помилка типу IndexError!")

def handle_error():
    try:
        oops()  # Викликаємо функцію, яка генерує виключення
    except IndexError as e:
        print(f"Перехоплено помилку: {e}")

handle_error()

#task2 
def func():
    try:
        # Отримуємо числа від користувача
        a = float(input("Введіть число a: "))
        b = float(input("Введіть число b: "))
        
        # Перевіряємо, чи не дорівнює b нулю
        if b == 0:
            raise ZeroDivisionError("На нуль ділити не можна!")
        
        # Обчислюємо результат
        result = (a ** 2) / b
        return result
    
    except ValueError:
        print("Помилка: введено не число!")
    except ZeroDivisionError as e:
        print(e)

# Викликаємо функцію
result = func()
if result is not None:
    print(f"Результат: {result}")
