class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"

point = Point(2, 3)
print(point) # без репр виведе об'єкт <__main__.Point object at 0x00000268D7B89A30>
print(repr(point))  # Виводить: Point(x=2, y=3)

'''''''''.........'''''''''

class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"

original_point = Point(2, 3)
print(repr(original_point))  

# Використання рядка, повернутого __repr__, для створення нового об'єкта
new_point = eval(repr(original_point))
print(new_point)
