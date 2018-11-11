class Student:
    schoolname = 'John Dewey'

    def printschooldetailsInfo(self):
        print(self.schoolname, "Villupuram")


student = Student()
student.printschooldetailsInfo()


class PostGraduduate(Student):
    schoolname = "Kamaraj College of Engineering & Technology"

    def printschooldetails(self):
        print(self.schoolname, "Virudhunagar")

    def printugschooldetails(self):
        super().printschooldetailsInfo()


pg = PostGraduduate()
pg.printschooldetails()
pg.printugschooldetails()
