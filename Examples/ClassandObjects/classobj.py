class Student:
    def __init__(self):
        print('am in constructor')
    def printstudent(self):
        print('Student')
    def __str__(self):
        return "Student"


student = Student()
print(student.printstudent())
print(student)