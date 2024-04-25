import copy

my_list = [1, 2, {"name": "Gupalo Vasyl"}]
copy_list = copy.deepcopy(my_list) #копія як новий об'єкт
copy_list[2]["age"] = 30
print(my_list)
print(copy_list)
