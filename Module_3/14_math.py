# Модуль math
import math

# Вихідне число
x = 3.7

# Використання різних методів округлення
ceil_result = math.ceil(x)  # Округлення вгору
floor_result = math.floor(x)  # Округлення вниз
trunc_result = math.trunc(x)  # Відсікання дробової частини

print(ceil_result, floor_result, trunc_result)


# Використання констант
print(math.pi)  # Виведе приблизне значення π

# Тригонометрія
angle = math.radians(60)  # Конвертація з градусів у радіани
print(math.sin(angle))  # Синус кута

# Корінь числа
print(math.sqrt(9))  # Квадратний корінь з 9

# Логарифми
print(math.log(10, 2))  # Логарифм 10 за основою 2

x = 1
y = 2

math.sin(x) # синус x, де x в радіанах;
math.cos(x) # косинус x;
math.tan(x) # тангенс x;
math.asin(x) # арксинус x;
math.acos(x) # арккосинус x;
math.atan(x) # арктангенс x;
math.exp(x) # число e в ступені x;
math.log(x) # Логарифм x за основою base. Якщо base не вказано, обчислюється натуральний логарифм;
math.pow(x, y) # x у ступені y;
math.sqrt(x) # квадратний корінь з x;
math.fabs(x) # модуль (абсолютне значення) x;
f = math.factorial(x) # факторіал числа x;
math.gcd(x, y) # найбільший спільний дільник для x та y;
print(f)