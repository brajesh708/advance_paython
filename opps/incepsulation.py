# Encapsulation is a fundamental object-oriented principle in Python. It protects your classes from accidental changes or deletions and promotes code reusability and maintainability. Consider this simple class definition:


# access modifire
#  1 public   name="brajesh"
# 2 proteced   _name="brajesh"    ese python recomnded nahi karta
# 3 private    __name="brajesh"    eske liye 2 bar under score laga dete he 


# private exampale 
class Student:
    school="sshc"
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
    def detels(self):
        print("name=",self.__name)
        print("age =",self.__age)
        print("school=",Student.school)
class Maeks(Student):
    def marks(self,hindi,math):
        self.hindi=hindi
        self.math=math
    def complet_detels(self):
        print("name=",self.__name)
        print("age",self.__age)
        print("schol=",Student.school)
        print("hindi",self.hindi)
        print("math=",self.math)
obj= Maeks("brajesh",22)
obj.__name="vaisu"
obj.detels()
obj.marks(86,98)
Student.school="authentic school"
obj.complet_detels
        


