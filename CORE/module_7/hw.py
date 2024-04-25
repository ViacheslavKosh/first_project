# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
    
#     @property
#     def x(self):
#         return self.__x
    
#     @property
#     def y(self):
#         return self.__y   
    
#     @x.setter
#     def x(self, new_x):
#         self.__x = new_x
    
#     @y.setter
#     def y(self, new_y):
#         self.__y = new_y

# point = Point(5, 10)

# print(point.x)  # 5
# print(point.y)  # 10





# class Point:
#     def __init__(self, x, y):
#         self.__x = None
#         self.__y = None
#         self.x = x
#         self.y = y

#     @property
#     def x(self):
#         return self.__x

#     @x.setter
#     def x(self, x):
#         self.__x = self.validate_numeric_value(x)
            
#     @property
#     def y(self):
#         return self.__y

#     @y.setter
#     def y(self, y):
#         self.__y = self.validate_numeric_value(y)

#     def validate_numeric_value(self, value):
#         if isinstance(value, (int, float)):
#             return int(value)
#         else:
#             return None
        

# point = Point("a", 10)

# print(point.x)  # None
# print(point.y)  # 10




# class Point:
#     def __init__(self, x, y):
#         self.__x = None
#         self.__y = None
#         self.x = x
#         self.y = y
    
#     @property
#     def x(self):
#         return self.__x
    
#     @x.setter
#     def x(self, x):
#         if type(x) == int or type(x) == float:
#             self.__x = x
#         return None
    
#     @property
#     def y(self):
#         return self.__y
    
#     @y.setter
#     def y(self, y):
#         if type(y) == int or type(y) == float:
#             self.__y = y
#         return None

# point = Point("a", 10)

# print(point.x)  # None
# print(point.y)  # 10





class Point:
    def __init__(self, x, y):
        self.__x = None
        self.__y = None
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if (type(x) == int) or (type(x) == float):
            self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if (type(y) == int) or (type(y) == float):
            self.__y = y

    def __str__(self):
        return f'Point({self.x}, {self.y})'
    
    def __repr__(self):
        return f"Point({self.x}, {self.y})"

class Vector:
    def __init__(self, coordinates: Point):
        self.coordinates = coordinates

    def __setitem__(self, index, value):
        if index == 0:
            self.coordinates.x = value
        elif index == 1:
            self.coordinates.y = value
        else:
            raise IndexError("Vector index out of range")

    def __getitem__(self, index):
        if index == 0:
            return self.coordinates.x
        elif index == 1:
            return self.coordinates.y
        else:
            raise IndexError("Vector index out of range")
    
    def __call__(self, value=None):
        if value:
            new_x = self.coordinates.x * value
            new_y = self.coordinates.y * value
            return (new_x, new_y)
        return (self.coordinates.x, self.coordinates.y)

    def __add__(self, vector):
        new_x = self.coordinates.x + vector.coordinates.x
        new_y = self.coordinates.x + vector.coordinates.y
        return Vector(Point(new_x, new_y))     

    def __sub__(self, vector):
        new_x = self.coordinates.x - vector.coordinates.x
        new_y = self.coordinates.x - vector.coordinates.y
        return Vector(Point(new_x, new_y)) 

    def __mul__(self, vector):
        scal_mul = (self.coordinates.x * vector.coordinates.x) + (self.coordinates.y * vector.coordinates.y)
        return scal_mul      

    def len(self):
        return ((self.coordinates.x ** 2 + self.coordinates.y ** 2)**0.5)

    def __str__(self):
        return f'Vector({self.coordinates.x}, {self.coordinates.y})'
    
    def __eq__(self, vector):
        return self.len() == vector.len()    

    def __ne__(self, vector):
        return self.len() != vector.len() 

    def __lt__(self, vector):
        return self.len() < vector.len()  

    def __gt__(self, vector):
        return self.len() > vector.len() 

    def __le__(self, vector):
        return self.len() <= vector.len() 

    def __ge__(self, vector):
        return self.len() >= vector.len()
    
vector1 = Vector(Point(1, 10))
vector2 = Vector(Point(10, 10))

vector3 = vector2 + vector1
vector4 = vector2 - vector1

print(vector3)  # Vector(11,20)
print(vector4)  # Vector(9,0)

scalar = vector2 * vector1
print(scalar)  # 110

print(vector1.len())  # 10.04987562112089
print(vector2.len())  # 14.142135623730951

vector1 = Vector(Point(1, 10))
vector2 = Vector(Point(3, 10))

print(vector1 == vector2)  # False
print(vector1 != vector2)  # True
print(vector1 > vector2)  # False
print(vector1 < vector2)  # True
print(vector1 >= vector2)  # False
print(vector1 <= vector2)  # True