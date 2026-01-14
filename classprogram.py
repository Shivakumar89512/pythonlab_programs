class Person:
    def __init__(self,name,age,habbit):
        self.name=name
        self.age=age
        self.habbit=habbit

    def show(self):
        print("Name:",self.name,"Age:",self.age,"Habbit:",self.habbit)

    def like(self):
        print(self.name,"likes",self.habbit)

shivu=Person("shivu",21,"singing")

shivu.show()
shivu.like()

