# task 1
def favorite_movie(name):
    print(f"My favorite movie is named {name}")
favorite_movie("Admiral")
# task 2
def make_country(country_name, capital_name):
    country_dict = {country_name: capital_name}
    print(country_dict)
make_country("Ukraima","KIev")
# task 3
def make_operation(operator, *argument):
    if operator == '+':
        return sum(argument)
    elif operator == '-':
        result = argument[0]
        for num in argument[1:]:
            result -= num
        return result
    elif operator == '*':
        result = 1
        for num in argument:
            result *= num
        return result
    else:
        return "Invalid operator"
print(make_operation('+', 7, 7, 2))
print(make_operation('-', 5, 5, -10, -20))
print(make_operation('*', 7, 6))