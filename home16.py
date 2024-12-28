#task1
import re
class User:
    def __init__(self, email):
        self.email = email
        self.validate()
    def validate(self):
        if not isinstance(self.email, str):
            raise ValueError("Email must be a string")
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if not re.match(email_regex, self.email):
            raise ValueError(f"'{self.email}' is not a valid email address")

    def __str__(self):
        return f"User with email: {self.email}"

# Тестування
try:
    user1 = User("valid.email@example.com")
    print(user1)
    
    user2 = User("invalid-email.com") 
    print(user2)
except ValueError as e:
    print(f"Error: {e}")

#task2
class Boss:
    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self.workers = []

    def add_worker(self, worker: 'Worker'):
        if isinstance(worker, Worker) and worker.boss == self:
            self.workers.append(worker)
        else:
            raise ValueError(f"{worker.name} is not assigned to this boss.")

    def get_workers(self):
        return self.workers

    def set_workers(self, workers: list):
        for worker in workers:
            if not isinstance(worker, Worker) or worker.boss != self:
                raise ValueError(f"All workers must be assigned to this boss.")
        self.workers = workers


class Worker:
    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.id = id_
        self.name = name
        self.company = company
        self.boss = None 

        self.set_boss(boss)

    def set_boss(self, boss: Boss):
        if not isinstance(boss, Boss):
            raise ValueError(f"{boss.name} is not a valid Boss.")
        self.boss = boss
        boss.add_worker(self)

    def get_boss(self):
        return self.boss

# Тестування:

boss1 = Boss(id_=1, name="John Smith", company="TechCorp")
worker1 = Worker(id_=101, name="Alice", company="TechCorp", boss=boss1)
worker2 = Worker(id_=102, name="Bob", company="TechCorp", boss=boss1)

# Додавання робітників
print(f"Workers under {boss1.name}: {[worker.name for worker in boss1.get_workers()]}")

# Спроба встановити нового боса для працівника
worker1.set_boss(boss1)  # Це має успішно працювати, бо worker1 вже має цього боса

# Спроба додавання неправильного працівника
try:
    worker1.set_boss("not_a_boss")  # Це має викликати помилку
except ValueError as e:
    print(f"Error: {e}")

worker3 = Worker(id_=103, name="Charlie", company="TechCorp", boss=boss1)
print(f"Workers under {boss1.name}: {[worker.name for worker in boss1.get_workers()]}")

#task3
from functools import wraps

class TypeDecorators:

    @staticmethod
    def to_int(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            try:
                return int(result)
            except ValueError:
                return None 
        return wrapper

    @staticmethod
    def to_str(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return str(result)
        return wrapper

    @staticmethod
    def to_bool(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if isinstance(result, str):
                return result.strip().lower() in ['true', '1', 'yes', 'y']
            return bool(result)
        return wrapper

    @staticmethod
    def to_float(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            try:
                return float(result)
            except ValueError:
                return None  
        return wrapper

# Тестування

@TypeDecorators.to_int
def do_nothing(string: str):
    return string

@TypeDecorators.to_bool
def do_something(string: str):
    return string

# Перевірка
assert do_nothing('25') == 25
assert do_something('True') is True
assert do_something('False') is False
assert do_something('yes') is True
assert do_something('no') is False

print("All tests passed!")