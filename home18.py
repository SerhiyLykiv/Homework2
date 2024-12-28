#task1
import unittest

class CustomIterator:
    def __init__(self, data):
        self.data = data  
        self.index = 0 

    def __iter__(self):
        return self  

    def __next__(self):
        if self.index < len(self.data):
            result = self.data[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration  

    def __getitem__(self, index):
        if index < len(self.data):
            return self.data[index]
        else:
            raise IndexError("Index out of range")  


class TestCustomIterator(unittest.TestCase):
    def setUp(self):
        """Налаштовуємо тестові дані"""
        self.data = [1, 2, 3, 4, 5]
        self.iterator = CustomIterator(self.data)

    def test_iteration(self):
        """Тестуємо ітерацію за допомогою циклу for"""
        result = []
        for item in self.iterator:
            result.append(item)
        self.assertEqual(result, self.data)

    def test_access_by_index(self):
        """Тестуємо доступ до елементів за індексом"""
        self.assertEqual(self.iterator[0], 1)
        self.assertEqual(self.iterator[2], 3)
        self.assertEqual(self.iterator[4], 5)

    def test_index_out_of_range(self):
        """Тестуємо доступ до елементів за індексом поза межами списку"""
        with self.assertRaises(IndexError):
            self.iterator[5] 

    def test_empty_iterator(self):
        """Тестуємо ітератор для порожнього списку"""
        empty_iterator = CustomIterator([])
        result = list(empty_iterator)
        self.assertEqual(result, [])  
if __name__ == "__main__":
    unittest.main()

#task2
import unittest

class Phonebook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone_number):
        if name in self.contacts:
            raise ValueError(f"Contact with name {name} already exists.")
        self.contacts[name] = phone_number

    def remove_contact(self, name):
        if name not in self.contacts:
            raise ValueError(f"Contact with name {name} not found.")
        del self.contacts[name]

    def find_contact(self, name):
        return self.contacts.get(name, None)

    def get_all_contacts(self):
        return self.contacts


class TestPhonebook(unittest.TestCase):
    
    def setUp(self):
        """Цей метод викликається перед кожним тестом для налаштування даних"""
        self.phonebook = Phonebook()

    def test_add_contact(self):
        """Тестуємо додавання нового контакту"""
        self.phonebook.add_contact("Alice", "123-456-789")
        self.assertEqual(self.phonebook.find_contact("Alice"), "123-456-789")

    def test_add_existing_contact(self):
        """Тестуємо додавання контакту з уже існуючим ім'ям"""
        self.phonebook.add_contact("Alice", "123-456-789")
        with self.assertRaises(ValueError):
            self.phonebook.add_contact("Alice", "987-654-321")

    def test_remove_contact(self):
        """Тестуємо видалення контакту"""
        self.phonebook.add_contact("Bob", "987-654-321")
        self.phonebook.remove_contact("Bob")
        self.assertIsNone(self.phonebook.find_contact("Bob"))

    def test_remove_non_existing_contact(self):
        """Тестуємо видалення неіснуючого контакту"""
        with self.assertRaises(ValueError):
            self.phonebook.remove_contact("Charlie")

    def test_find_contact(self):
        """Тестуємо пошук контакту"""
        self.phonebook.add_contact("David", "321-654-987")
        self.assertEqual(self.phonebook.find_contact("David"), "321-654-987")
        self.assertIsNone(self.phonebook.find_contact("Eve"))

    def test_get_all_contacts(self):
        """Тестуємо отримання всіх контактів"""
        self.phonebook.add_contact("Alice", "123-456-789")
        self.phonebook.add_contact("Bob", "987-654-321")
        expected_contacts = {
            "Alice": "123-456-789",
            "Bob": "987-654-321"
        }
        self.assertEqual(self.phonebook.get_all_contacts(), expected_contacts)

if __name__ == "__main__":
    unittest.main()