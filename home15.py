#task1
class Animal:
    def talk(self):
        raise NotImplementedError("Метод talk має бути реалізований в підкласі.")

class Dog(Animal):
    def talk(self):
        return "гав-гав"

class Cat(Animal):
    def talk(self):
        return "няв-няв"

def make_animal_talk(animal: Animal):
    if isinstance(animal, Animal):
        return animal.talk()
    else:
        raise ValueError("Переданий об'єкт не є екземпляром класу Animal.")

dog = Dog()
cat = Cat()

print(make_animal_talk(dog))  
print(make_animal_talk(cat))  

#task2
# Клас Автор
class Author:
    def __init__(self, name: str, country: str, birth_date: str):
        self.name = name
        self.country = country
        self.birth_date = birth_date
        self.books = []  # Список книг цього автора
    
    def __repr__(self):
        return f"Author(name={self.name}, country={self.country}, birth_date={self.birth_date})"
    
    def __str__(self):
        return f"{self.name} ({self.country}, born {self.birth_date})"


# Клас Книга
class Book:
    book_count = 0  
    
    def __init__(self, name: str, year: int, author: Author):
        self.name = name
        self.year = year
        self.author = author
        self.author.books.append(self)  
        Book.book_count += 1  
    
    def __repr__(self):
        return f"Book(name={self.name}, year={self.year}, author={self.author.name})"
    
    def __str__(self):
        return f"'{self.name}' ({self.year}) by {self.author.name}"


# Клас Бібліотека
class Library:
    def __init__(self, name: str):
        self.name = name
        self.books = []  
        self.authors = []  
    
    def new_book(self, name: str, year: int, author: Author):
        book = Book(name, year, author)
        self.books.append(book)
        if author not in self.authors:
            self.authors.append(author)
        return book
    
    def group_by_author(self, author: Author):
        return [book for book in self.books if book.author == author]
    
    def group_by_year(self, year: int):
        return [book for book in self.books if book.year == year]
    
    def __repr__(self):
        return f"Library(name={self.name}, books_count={len(self.books)}, authors_count={len(self.authors)})"
    
    def __str__(self):
        return f"Library '{self.name}' with {len(self.books)} books and {len(self.authors)} authors"


# Приклад використання

author1 = Author("J.K. Rowling", "UK", "1965-07-31")
author2 = Author("George Orwell", "UK", "1903-06-25")

library = Library("City Library")

book1 = library.new_book("Harry Potter and the Philosopher's Stone", 1997, author1)
book2 = library.new_book("Harry Potter and the Chamber of Secrets", 1998, author1)
book3 = library.new_book("1984", 1949, author2)

print(library.group_by_author(author1))  
print(library.group_by_year(1997))  
print(library)  
print(book1) 
print(Book.book_count)  

#task3
from math import gcd

class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")
        self.numerator = numerator
        self.denominator = denominator
        self._normalize()

    def _normalize(self):
        common_divisor = gcd(self.numerator, self.denominator)
        self.numerator //= common_divisor
        self.denominator //= common_divisor
        if self.denominator < 0:
            self.numerator = -self.numerator
            self.denominator = -self.denominator

    def __add__(self, other):
        if isinstance(other, Fraction):
            new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
            new_denominator = self.denominator * other.denominator
            return Fraction(new_numerator, new_denominator)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Fraction):
            new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
            new_denominator = self.denominator * other.denominator
            return Fraction(new_numerator, new_denominator)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Fraction):
            new_numerator = self.numerator * other.numerator
            new_denominator = self.denominator * other.denominator
            return Fraction(new_numerator, new_denominator)
        return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, Fraction):
            if other.numerator == 0:
                raise ValueError("Cannot divide by zero fraction")
            new_numerator = self.numerator * other.denominator
            new_denominator = self.denominator * other.numerator
            return Fraction(new_numerator, new_denominator)
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Fraction):
            return self.numerator * other.denominator == other.numerator * self.denominator
        return NotImplemented

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        if isinstance(other, Fraction):
            return self.numerator * other.denominator < other.numerator * self.denominator
        return NotImplemented

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)

    def __gt__(self, other):
        if isinstance(other, Fraction):
            return self.numerator * other.denominator > other.numerator * self.denominator
        return NotImplemented

    def __ge__(self, other):
        return self.__gt__(other) or self.__eq__(other)

    def __repr__(self):
        return f"Fraction({self.numerator}, {self.denominator})"

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

# Тестування класу
if __name__ == "__main__":
    x = Fraction(1, 2)
    y = Fraction(1, 4)
    
    # Операції
    print(x + y)  
    print(x - y)  
    print(x * y)  
    print(x / y)  

    # Порівняння
    print(x == y)  
    print(x != y)  
    print(x < y)   
    print(x > y)   

    z = Fraction(6, 8)
    print(z)  

    # Перевірка на помилки
    try:
        z = Fraction(1, 0)  
    except ValueError as e:
        print(e)

    try:
        print(x / Fraction(0, 1)) 
    except ValueError as e:
        print(e)
