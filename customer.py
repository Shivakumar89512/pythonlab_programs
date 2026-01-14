#customer name,id,age,address
#display  customer details

class Cus:
    def __init__(self,name,id,age,address):
        self.name=name
        self.id=id
        self.age=age
        self.address=address

    def details(self):
        print("Name:",self.name,"ID",self.id,"Age:",self.age,"Adderess:",self.address)

C=Cus("charlie","A01",28,"Near bus stop")

C.details()


