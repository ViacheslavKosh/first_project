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
        if type(x) == int or type(x) == float:
            self.__x = x
        return None
    
    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self, y):
        if type(y) == int or type(y) == float:
            self.__y = y
        return None

point = Point("a", 10)

print(point.x)  # None
print(point.y)  # 10