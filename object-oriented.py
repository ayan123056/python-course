class Student:
    grade = 10
    name = "johannes guttenberg"
    def introduction (self):
        print("hi ,i am a Student") 
    def details (self):
        print("my name is ",self.name)
        print("I study in grade",self.grade)
ob = Student()
ob.introduction()
ob.details()