#task1
class Person:
    def __init__(self, name, age):
        self.name = name 
        self.age = age 

    def greet(self):
        return f"Привіт, я {self.name}, мені {self.age} років."

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)  
        self.student_id = student_id  
        self.grades = [] 

    def add_grade(self, grade):
        self.grades.append(grade)  

    def get_average_grade(self):
        if len(self.grades) > 0:
            return sum(self.grades) / len(self.grades)  
        return 0

    def greet(self):
        return f"Привіт, я студент {self.name}, мені {self.age} років. Мій студентський номер: {self.student_id}."

class Teacher(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)  
        self.salary = salary  
        self.subject = None  

    def set_subject(self, subject):
        self.subject = subject  

    def get_salary(self):
        return f"Моя зарплата: {self.salary}."

    def greet(self):
        return f"Привіт, я вчитель {self.name}, мені {self.age} років. Я викладаю {self.subject}."

# Приклад використання

# Створення об'єктів
student = Student("Тарас", 17, "0168750")
teacher = Teacher("Іванка", 35, 50000)

student.add_grade(3)
student.add_grade(5)
student.add_grade(3)

# Виведення результатів
print(student.greet())  
print(f"Середня оцінка: {student.get_average_grade()}")  

teacher.set_subject("Інформатика")
print(teacher.greet())  
print(teacher.get_salary())  

#task2
class Mathematician:
    
    def square_nums(self, nums):
        """Повертає список квадратів чисел з наданого списку."""
        return [num ** 2 for num in nums]

    def remove_positives(self, nums):
        """Повертає список без додатних чисел."""
        return [num for num in nums if num <= 0]

    def filter_leaps(self, years):
        """Повертає список тільки високосних років."""
        def is_leap_year(year):
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                return True
            return False

        return [year for year in years if is_leap_year(year)]


# Тестування

m = Mathematician()

assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]
assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]
assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]
print("Усі тести пройдені успішно.")

#task3

class Product:
    def __init__(self, type_, name, price):
        self.type = type_  # Тип товару
        self.name = name  # Назва товару
        self.price = price  # Ціна товару
    
    def __str__(self):
        return f"{self.name} ({self.type}) - {self.price} грн"


class ProductStore:
    def __init__(self):
        self.products = {}  # Словник для зберігання товарів
        self.income = 0  # Дохід

    def add(self, product, amount):
        """Додає товар в магазин з кількістю та націнкою 30%"""
        if not isinstance(product, Product):
            raise ValueError("Очікується об'єкт класу Product.")
        
        # Розраховуємо ціну з націнкою
        price_with_markup = product.price * 1.30

        if product.name in self.products:
            self.products[product.name]['amount'] += amount
        else:
            self.products[product.name] = {
                'product': product,
                'amount': amount,
                'price': price_with_markup
            }

    def sell_product(self, name, amount):
        """Продає товар з певною назвою та кількістю"""
        if name not in self.products:
            raise ValueError(f"Товар з назвою '{name}' не знайдено в магазині.")

        product_info = self.products[name]
        if product_info['amount'] < amount:
            raise ValueError(f"Недостатньо товару '{name}' для продажу.")

        # Оновлюємо кількість товару
        product_info['amount'] -= amount
        
        # Рахуємо дохід
        self.income += product_info['price'] * amount

    def get_income(self):
        """Повертає дохід магазину"""
        return self.income

    def get_all_products(self):
        """Повертає інформацію про всі товари в магазині"""
        return [(product_info['product'].name, product_info['amount']) for product_info in self.products.values()]

    def get_product_info(self, name):
        """Повертає інформацію про конкретний товар"""
        if name not in self.products:
            raise ValueError(f"Товар з назвою '{name}' не знайдено в магазині.")
        product_info = self.products[name]
        return (product_info['product'].name, product_info['amount'])

p = Product('Спорт', 'Футбольна футболка', 100)
p2 = Product('Food', 'Ramen', 1.5)

s = ProductStore()

s.add(p, 10)
s.add(p2, 300)

s.sell_product('Ramen', 10)

assert s.get_product_info('Ramen') == ('Ramen', 290)

print(s.get_income()) 

#task4
class CustomException(Exception):
    def __init__(self, msg):
        super().__init__(msg)
        with open("logs.txt", "a") as log_file:
            log_file.write(f"Error: {msg}\n")
try:
    raise CustomException("This is a custom error message.")
except CustomException as e:
    print(f"Caught an error: {e}")
