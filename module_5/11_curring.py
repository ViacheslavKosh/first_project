# Проста функція
def add(a, b):
    return a + b


# Каррінг постої функції
def add(a):
    def add_b(b):
        return a + b
    return add_b
# Використання:
add_5 = add(5)
result = add_5(10)
print(result)


# проста функція 2
def apply_discount(price: float, discount_percentage: int) -> float:
    return price * (1 - discount_percentage / 100)
# Використання
discounted_price = apply_discount(500, 10)  # Знижка 10% на ціну 500
print(discounted_price)
discounted_price = apply_discount(500, 20)  # Знижка 20% на ціну 500
print(discounted_price)


# Каррінг функції 2 для гнучкості застосування
from typing import Callable
def discount(discount_percentage: int) -> Callable[[float], float]:
    def apply_discount(price: float) -> float:
        return price * (1 - discount_percentage / 100)
    return apply_discount
# Каррінг в дії
ten_percent_discount = discount(10)
twenty_percent_discount = discount(20)
# Застосування знижок
discounted_price = ten_percent_discount(500)  # 450.0
print(discounted_price)
discounted_price = twenty_percent_discount(500)  # 400.0
print(discounted_price)


# Додавання словника зі знижками
from typing import Callable, Dict
def discount(discount_percentage: int) -> Callable[[float], float]:
    def apply_discount(price: float) -> float:
        return price * (1 - discount_percentage / 100)
    return apply_discount
# Створення словника з функціями знижок
discount_functions: Dict[str, Callable] = {
    "10%": discount(10),
    "20%": discount(20),
    "30%": discount(30)
}
# Використання функції зі словника
price = 500
discount_type = "20%"
discounted_price = discount_functions[discount_type](price)
print(f"Ціна зі знижкою {discount_type}: {discounted_price}")
