class Classroom:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def find_age(self):
        students_age = []
        for student in self.students:
            students_age.append(student.age)
        return sum(students_age) // len(students_age)



class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

jhon = Student("Jhon", 17)
mark = Student("Mark", 19)

c = Classroom()

c.add_student(jhon)
c.add_student(mark)

print(c.find_age())