#task1
import logging

class CustomOpen:
    open_count = 0

    def __init__(self, file_name, mode='r'):
        self.file_name = file_name
        self.mode = mode
        self.file = None
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(message)s')

    def __enter__(self):
        """Метод для відкриття файлу та збільшення лічильника."""
        CustomOpen.open_count += 1
        logging.info(f"Opening file {self.file_name} in {self.mode} mode.")
        self.file = open(self.file_name, self.mode)
        logging.info(f"File {self.file_name} opened successfully.")
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        """Метод для закриття файлу та логування після закриття."""
        if self.file:
            logging.info(f"Closing file {self.file_name}.")
            self.file.close()
        if exc_type:
            logging.error(f"Error occurred: {exc_value}")
        else:
            logging.info(f"File {self.file_name} closed successfully.")

    @classmethod
    def get_open_count(cls):
        """Метод для отримання кількості відкритих файлів."""
        return cls.open_count

if __name__ == '__main__':
    with CustomOpen('test_file.txt', 'w') as file:
        file.write("Hello, World!\n")
        file.write("This is a test.")
    with CustomOpen('test_file.txt', 'r') as file:
        content = file.read()
        print(content)
    print(f"Files opened: {CustomOpen.get_open_count()}")

#task2
import unittest
import os
from unittest.mock import patch
class CustomOpen:
    open_count = 0

    def __init__(self, file_name, mode='r'):
        self.file_name = file_name
        self.mode = mode
        self.file = None
        import logging
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(message)s')

    def __enter__(self):
        """Метод для відкриття файлу та збільшення лічильника."""
        CustomOpen.open_count += 1
        import logging
        logging.info(f"Opening file {self.file_name} in {self.mode} mode.")
        self.file = open(self.file_name, self.mode)
        logging.info(f"File {self.file_name} opened successfully.")
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        """Метод для закриття файлу та логування після закриття."""
        if self.file:
            import logging
            logging.info(f"Closing file {self.file_name}.")
            self.file.close()
        if exc_type:
            import logging
            logging.error(f"Error occurred: {exc_value}")
        else:
            import logging
            logging.info(f"File {self.file_name} closed successfully.")

    @classmethod
    def get_open_count(cls):
        """Метод для отримання кількості відкритих файлів."""
        return cls.open_count


# Тестовий клас
class TestCustomOpen(unittest.TestCase):

    def setUp(self):
        """Підготовка до тестів: створюємо тимчасовий файл для тестування"""
        self.test_file_name = 'test_file.txt'
        self.test_content = 'Hello, World!\nThis is a test.'
        with open(self.test_file_name, 'w') as f:
            f.write(self.test_content)

    def tearDown(self):
        """Після кожного тесту очищуємо тимчасовий файл"""
        if os.path.exists(self.test_file_name):
            os.remove(self.test_file_name)

    def test_file_write_and_read(self):
        """Тест на успішне відкриття, запис і читання з файлу"""
        with CustomOpen(self.test_file_name, 'w') as file:
            file.write("New content written to file.")

        with CustomOpen(self.test_file_name, 'r') as file:
            content = file.read()
            self.assertEqual(content, "New content written to file.")

    def test_open_count(self):
        """Перевірка лічильника відкритих файлів"""
        self.assertEqual(CustomOpen.get_open_count(), 0)
        
        with CustomOpen(self.test_file_name, 'r') as file:
            pass
        
        self.assertEqual(CustomOpen.get_open_count(), 1)
        
        with CustomOpen(self.test_file_name, 'r') as file:
            pass
        
        self.assertEqual(CustomOpen.get_open_count(), 2)

    def test_file_not_found(self):
        """Тест на спробу відкрити неіснуючий файл"""
        with self.assertRaises(FileNotFoundError):
            with CustomOpen('non_existent_file.txt', 'r') as file:
                pass

    def test_invalid_mode(self):
        """Тест на некоректний режим відкриття файлу"""
        with self.assertRaises(ValueError):
            with CustomOpen(self.test_file_name, 'invalid_mode') as file:
                pass

    def test_error_in_file_operation(self):
        """Тест на виникнення помилки в процесі роботи з файлом"""
        os.chmod(self.test_file_name, 0o444)  
        try:
            with self.assertRaises(OSError):
                with CustomOpen(self.test_file_name, 'w') as file:
                    file.write("Trying to write to a read-only file.")
        finally:
            os.chmod(self.test_file_name, 0o666)

if __name__ == '__main__':
    unittest.main()
