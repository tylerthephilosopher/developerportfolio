#Hi i am doing a mock class for students that go to humber college
#step one is to define a class Student
#Student class
class Student:
    school = "Humber College"

    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname 
        self.age = age

    def courses(self, cname, code):
        self.cname = cname
        self.code = code 

    def grade(self, sgrade):
        self.sgrade = sgrade

    def report(self):
        return f"\nStudent: {self.fname} {self.lname} \nLocation: {Student.school} \nCourse(s)/Code/Grade: {self.cname} ({self.code}): {self.sgrade}\n"


person1 = Student("Tyler", "Nietvelt", 27)
person1.courses("Introduction to Java","CMP1123")
person1.grade(80)
print(person1.report())

person2 = Student("Kyle", "Nietvelt", 29)
person2.courses("Politcal Discourse", "PlS4434")
person2.grade(87)
print(person2.report())
