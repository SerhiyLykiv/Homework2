#task1
def with_index(iterable, start=0):
    for index, value in zip(range(start, start + len(iterable)), iterable):
        yield index, value

# Тестування

for index, value in with_index(['a', 'b', 'c']):
    print(index, value)

for index, value in with_index(['a', 'b', 'c'], start=5):
    print(index, value)

#task2
def in_range(start, end, step=1):
    if step == 0:
        raise ValueError("step cannot be zero")
    
    if step > 0:
        while start < end:
            yield start
            start += step
    elif step < 0:
        while start > end:
            yield start
            start += step

# Тестування

print(list(in_range(1, 5)))  

print(list(in_range(1, 10, 2)))  

print(list(in_range(5, 0, -1)))  

try:
    print(list(in_range(1, 5, 0)))  
except ValueError as e:
    print(e)  

#task3
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

# Тестування

data = [1, 2, 3, 4, 5]
iterator = CustomIterator(data)

print("Iterating with for-in:")
for item in iterator:
    print(item)

print("\nAccessing elements with square brackets:")
print(iterator[0])  
print(iterator[2])  
print(iterator[4])  

try:
    print(iterator[5])  
except IndexError as e:
    print(e)
