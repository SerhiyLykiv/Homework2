#task1 
def locval():
    a = 5
    b = 10
    c = 15
    # Використовуємо locals() для отримання всіх локальних змінних
    local_vars = locals()
    return len(local_vars)

print("Кількість локальних змінних:", locval())

#task2
def perha(x):
    def dryha(y):
        return x + y

    return dryha  

add_five = perha(5)

result = add_five(10)
print(f"Результат: {result}")

#task3
def choose_func(nums: list, func1, func2):
    if all(num > 0 for num in nums):
        return func1(nums)
    else:
        return func2(nums)
#дані
nums1 = [1, 2, 3, 4, 5]
nums2 = [1, -2, -3, -4, -5]
nums3 = [1, -2, 3, -4, 5]
# Функції для тестування
def square_nums(nums):
    return [num ** 2 for num in nums]

def remove_negatives(nums):
    return [num for num in nums if num > 0]
# Тест
assert choose_func(nums1, square_nums, remove_negatives) == [1, 4, 9, 16, 25]
assert choose_func(nums2, square_nums, remove_negatives) == [1, 3, 5]
assert choose_func(nums3, square_nums, remove_negatives) == [1, 3, 5]