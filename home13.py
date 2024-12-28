#task1
class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def talk(self):
        print(f"Привіт, мене звати {self.first_name} {self.last_name} і мені {self.age} років")
person = Person("Карл", "Джонсон", 26)
person.talk()

#task2
class Dog:
    age_factor = 7

    def __init__(self, dog_age):
        self.dog_age = dog_age

    def human_age(self):
        return self.dog_age * Dog.age_factor

dog = Dog(5)

print(f"Вік собаки в людських роках: {dog.human_age()} років")

#task3
class TVController:
    def __init__(self, channels):
        self.channels = channels  
        self.current_index = 0  
        
    def first_channel(self):
        self.current_index = 0  
        return self.channels[self.current_index]

    def last_channel(self):
        self.current_index = len(self.channels) - 1 
        return self.channels[self.current_index]

    def turn_channel(self, N):
        if 1 <= N <= len(self.channels):
            self.current_index = N - 1
            return self.channels[self.current_index]
        return "Channel not found"

    def next_channel(self):
        self.current_index = (self.current_index + 1) % len(self.channels)
        return self.channels[self.current_index]

    def previous_channel(self):
        self.current_index = (self.current_index - 1) % len(self.channels)
        return self.channels[self.current_index]

    def current_channel(self):
        return self.channels[self.current_index]  

    def exists(self, N):
        if isinstance(N, int):
            if 1 <= N <= len(self.channels):
                return "Yes"
            else:
                return "No"
        elif isinstance(N, str):
            if N in self.channels:
                return "Yes"
            else:
                return "No"
        return "No"
CHANNELS = ["BBC", "Discovery", "TV1000"]
controller = TVController(CHANNELS)

# Тестування методів
print(controller.first_channel())  
print(controller.last_channel())   
print(controller.turn_channel(1))  
print(controller.next_channel())   
print(controller.previous_channel())  
print(controller.current_channel())  
print(controller.exists(4))  
print(controller.exists("BBC"))  
