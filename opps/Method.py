class Student:
    def display(self,name):
        self.name=name
        print("name=",name)
        
    def show(self,age):
        self.age=age
        self.display("raj")
        print("age=",age)
obj=Student()
obj.display("Brajesh")
obj.show(22)


#  class methode banane ki 
# @classmethod
# self  ke place per use cls

class Book:
    price=1000
    def book_detel(self,name,auther):
        self.name=name
        self.name=auther
        
        @classmethod
        def update_price(cls,price):
            cls.new_price=price  
        def show_detel(self):
            print("book name=",self.name)
            print("book auther =",self.auther)
            print("book price=",Book.price)
obj=Book()
obj.book_detel("pythone","gardio van rossas")
obj.show_detel()

            
