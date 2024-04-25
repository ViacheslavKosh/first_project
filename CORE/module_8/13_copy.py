my_list = [1, 2, 3]

def square_list(x: list):
    for i, el in enumerate(x):
        x[i] = el**2
    return x

new_list = square_list(my_list)
print(new_list)
print(my_list)


my_list = [1, 2, 3]

def square_list(x: list):
    return [el**2 for el in x]

new_list = square_list(my_list)
print(new_list)
print(my_list)
