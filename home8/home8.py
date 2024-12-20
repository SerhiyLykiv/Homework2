#task2
import sys
sys.path.append('D:\code\proect\Homeworc\home\home8\task1')
import task1.modyl1 as modyl1
print(modyl1.greet())
#task3

def count_lines(name):
    #Функція для підрахунку кількості рядків у файлі."""
    with open(name, 'r') as file:
        lines = file.readlines()
        return len(lines)

def count_chars(name):
    #Функція для підрахунку кількості символів у файлі."""
    with open(name, 'r') as file:
        content = file.read()
        return len(content)

def test(name):
    #Функція, яка викликає count_lines та count_chars для підрахунку рядків і символів."""
    lines = count_lines(name)
    chars = count_chars(name)
    print(f"File '{name}' has {lines} lines and {chars} characters.")

test('home8.py')