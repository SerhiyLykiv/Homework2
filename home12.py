#task1
def logger(func):
    def wrapper(*args, **kwargs):
        args_str = ", ".join(map(str, args))
        kwargs_str = ", ".join(f"{key}={value}" for key, value in kwargs.items())
        if kwargs_str:
            print(f"{func.__name__} викликано з {args_str}, {kwargs_str}")
        else:
            print(f"{func.__name__} викликано з {args_str}")
        return func(*args, **kwargs)  
    return wrapper
@logger
def add(x, y):
    return x + y

@logger
def square_all(*args):
    return [arg ** 2 for arg in args]

add(4, 5) 
square_all(1, 2, 3, 4)  

#task2
def stop_words(words: list):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            for word in words:
                result = result.replace(word, "*")
            return result
        return wrapper
    return decorator

@stop_words(['пепсі', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} п'є пепсі у своєму новому BMW!"

assert create_slogan("Стів") == "Стів п'є * у своєму новенькому *!"

#task3
def arg_rules(type_: type, max_length: int, contains: list):
    def decorator(func):
        def wrapper(*args, **kwargs):
            arg = args[0] if args else None
            if not isinstance(arg, type_):
                print(f"Помилка: аргумент повинен бути типу {type_}.")
                return False
            if len(arg) > max_length:
                print(f"Помилка: аргумент перевищує максимальну довжину {max_length}.")
                return False
            for char in contains:
                if char not in arg:
                    print(f"Помилка: аргумент не містить '{char}'.")
                    return False
            return func(*args, **kwargs)
        return wrapper
    return decorator

# Приклад використання декоратора

@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} п'є пепсі у своєму новому BMW!"

# Тестування

assert create_slogan('johndoe05@gmail.com') is False

assert create_slogan('S@SH05') == "S@SH05 п'є пепсі у своєму новому BMW!"

