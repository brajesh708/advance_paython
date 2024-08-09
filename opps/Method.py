# class Student:
#     def display(self,name):
#         self.name=name
#         print("name=",name)
        
#     def show(self,age):
#         self.age=age
#         self.display("raj")
#         print("age=",age)
# obj=Student()
# obj.display("Brajesh")
# obj.show(22)


#  class methode banane ki 
# @classmethod
# self  ke place per use cls

# class Book:
#     price=1000
#     def book_detail(self,name,author):
#         self.name=name
#         self.author=author
#     @classmethod
#     def update_price(cls,price):
#         cls.price=price
#     def show_data(self):
#         print('Book Name=',self.name)
#         print('Book Author=',self.author)
#         print('Book Price=',self.price)
# obj=Book()
# obj.book_detail('Python','Vaishu')
# obj.update_price(1500)
# obj.show_data()

    # static methode 
# class Student:
#     @staticmethod
#     def greet():
#         print("THanks for vizit this site")
        
#     def great1():
#         print("welcome to my wew page")
# obj=Student
# obj.greet()
# obj.great1()
# Student.greet()
# Student.great1()
# obj.great1()


class Student:
    @staticmethod
    def greet():
        print("THanks for vizit this site")
        
    def great1(self):
        print("welcome to my wew page")
obj=Student()
obj.greet()
obj.great1()
Student.greet()
# Student.great1()
obj.great1()
