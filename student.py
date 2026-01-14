
#create name,rollno age,create two objects and display details


class Student:
    def __init__(self,name,rollno,age):
        self.name=name
        self.rollno=rollno
        self.age=age

    def detail(self):
        print("Name:",self.name,"Roll NO:",self.rollno,"Age:",self.age)

    def status(self):
        print(self.name,"is good in behavoiur")

Stu=Student("shivu",57,21)
Stu1=Student("nikil",39,18)

Stu.detail()
Stu.status()

Stu1.detail()
Stu1.status()