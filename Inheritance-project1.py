class User:
    def login(self):
        print('Login')
    def register(self):
        print('Register')
class Student(User):    
    def enroll(self):
        print('Enroll')
    
    def review(self):
        print('Course Review')
        

stu1=Student()
stu1.enroll()
stu1.login()
stu1.register()
