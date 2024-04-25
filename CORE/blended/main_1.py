# Написати декоратор, який буде обгортати метод класу ти 
# виводити його результат та вхідні дані
def print_decorator(func):
    def wrapper(*args, **kwargs):
        print(f'Function: {func.__name__}')
        print('Input:', *args)
        result = func(*args, **kwargs)
        print('Output:', result)
        return result
    return wrapper

class Class:
    def __init__(self, value):
        self.value = value

    @print_decorator
    def multiply_value(self, number):
        return self.value * number
    
    def __str__(self):
        return f'Class({self.value})'
    
my_class = Class(5)
my_class.multiply_value(3)

# Input: 3
# Output: 15