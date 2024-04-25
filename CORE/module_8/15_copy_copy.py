import copy

my_list = [1, 2, {"name": "Gupalo Vasyl"}]
copy_list = copy.copy(my_list) #поверхнева копія
copy_list.append(4)
print(my_list)
print(copy_list)



my_list = [1, 2, {"name": "Gupalo Vasyl"}]
copy_list = copy.copy(my_list)
copy_list[2]["age"] = 30
print(my_list)
print(copy_list)
''' 
Поверхнева копія створює новий об'єкт, але не копіює вкладені об'єкти. 
Замість цього, вона копіює лише посилання на вкладені об'єкти. Це означає, 
що якщо ви змінюєте вкладені об'єкти в оригіналі, ці зміни також відобразяться 
у поверхневій копії
'''