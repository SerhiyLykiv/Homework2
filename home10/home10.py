#task1
#створення файлу
with open("myfile.txt", "w") as file:
    file.write("Hello file world!")
# Читання файлу
with open("myfile.txt", "r") as file:
    content = file.read()
    print(content)
#task2
import json
import os
# Структура даних для телефонної книги
class PhoneBook:
    def __init__(self, filename):
        self.filename = filename
        self.contacts = []
        self.load_data()
    # Завантажити дані з файлу JSON
    def load_data(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                self.contacts = json.load(file)
        else:
            print(f"Помилка: файл {self.filename} не знайдено.")
    # Зберегти дані у файл JSON
    def save_data(self):
        with open(self.filename, "w") as file:
            json.dump(self.contacts, file, indent=4)
    
    # Додавання нового запису
    def add_contact(self, first_name, last_name, phone_number, city, state):
        contact = {
            "first_name": first_name,
            "last_name": last_name,
            "phone_number": phone_number,
            "city": city,
            "state": state
        }
        self.contacts.append(contact)
        print("Запис успішно додано.")

    # Пошук за іменем
    def search_by_first_name(self, first_name):
        results = [contact for contact in self.contacts if contact["first_name"].lower() == first_name.lower()]
        return results
    
    # Пошук за прізвищем
    def search_by_last_name(self, last_name):
        results = [contact for contact in self.contacts if contact["last_name"].lower() == last_name.lower()]
        return results
    
    # Пошук за повним ім'ям
    def search_by_full_name(self, full_name):
        first_name, last_name = full_name.split()
        return self.search_by_first_name(first_name) + self.search_by_last_name(last_name)

    # Пошук за номером телефону
    def search_by_phone(self, phone_number):
        results = [contact for contact in self.contacts if contact["phone_number"] == phone_number]
        return results

    # Пошук за містом або штатом
    def search_by_city_or_state(self, city_or_state):
        results = [contact for contact in self.contacts if contact["city"].lower() == city_or_state.lower() or contact["state"].lower() == city_or_state.lower()]
        return results
    
    # Видалення запису за номером телефону
    def delete_by_phone(self, phone_number):
        self.contacts = [contact for contact in self.contacts if contact["phone_number"] != phone_number]
        print(f"Запис з номером телефону {phone_number} видалено.")
    
    # Оновлення запису за номером телефону
    def update_by_phone(self, phone_number):
        for contact in self.contacts:
            if contact["phone_number"] == phone_number:
                contact["first_name"] = input("Нове ім'я: ")
                contact["last_name"] = input("Нове прізвище: ")
                contact["city"] = input("Нове місто: ")
                contact["state"] = input("Новий штат: ")
                print("Запис успішно оновлено.")
                return
        print("Запис з таким номером телефону не знайдено.")
    
    # Виведення всіх контактів
    def display_all_contacts(self):
        for contact in self.contacts:
            print(f"Ім'я: {contact['first_name']}, Прізвище: {contact['last_name']}, Телефон: {contact['phone_number']}, Місто: {contact['city']}, Штат: {contact['state']}")

# Головна функція програми
def main():
    phonebook = PhoneBook("phonebook.json")
    
    while True:
        print("\n1. Додати запис")
        print("2. Пошук за іменем")
        print("3. Пошук за прізвищем")
        print("4. Пошук за повним ім'ям")
        print("5. Пошук за номером телефону")
        print("6. Пошук по місту або штату")
        print("7. Видалити запис")
        print("8. Оновити запис")
        print("9. Вивести всі записи")
        print("10. Вихід")
        
        choice = input("Виберіть опцію: ")

        if choice == "1":
            first_name = input("Ім'я: ")
            last_name = input("Прізвище: ")
            phone_number = input("Номер телефону: ")
            city = input("Місто: ")
            state = input("Штат: ")
            phonebook.add_contact(first_name, last_name, phone_number, city, state)

        elif choice == "2":
            first_name = input("Введіть ім'я для пошуку: ")
            results = phonebook.search_by_first_name(first_name)
            for contact in results:
                print(contact)

        elif choice == "3":
            last_name = input("Введіть прізвище для пошуку: ")
            results = phonebook.search_by_last_name(last_name)
            for contact in results:
                print(contact)

        elif choice == "4":
            full_name = input("Введіть повне ім'я (ім'я прізвище): ")
            results = phonebook.search_by_full_name(full_name)
            for contact in results:
                print(contact)

        elif choice == "5":
            phone_number = input("Введіть номер телефону для пошуку: ")
            results = phonebook.search_by_phone(phone_number)
            for contact in results:
                print(contact)

        elif choice == "6":
            city_or_state = input("Введіть місто або штат для пошуку: ")
            results = phonebook.search_by_city_or_state(city_or_state)
            for contact in results:
                print(contact)

        elif choice == "7":
            phone_number = input("Введіть номер телефону для видалення: ")
            phonebook.delete_by_phone(phone_number)

        elif choice == "8":
            phone_number = input("Введіть номер телефону для оновлення: ")
            phonebook.update_by_phone(phone_number)

        elif choice == "9":
            phonebook.display_all_contacts()

        elif choice == "10":
            phonebook.save_data()
            print("Дані збережено. Вихід з програми.")
            break

        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()