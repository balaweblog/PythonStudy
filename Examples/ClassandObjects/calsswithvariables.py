class Student:
    schoolname ='john dewey'
    def printstudentname(self):
        self.name = 'Balamurugan Alagumalai'
        print(self.name)
    def rollnumber(self):
        self.roll = '226016'
        print(self.name, self.roll)

student = Student()
print(student.schoolname)
student.printstudentname()
student.rollnumber()


# here schoolname is static variable
# here rollnumber is variables to be insisde the class and not static and organized by self keyword 
