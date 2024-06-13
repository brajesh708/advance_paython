
'''
class Car:
    def __init__(self, brand,modal):
        self.brand=brand
        self.modal=modal

my_car=Car("toyoya ","sift")
print(my_car.brand)
print(my_car.modal)

my_new_car=Car("boloro","maruti")
print(my_new_car.brand)
print(my_new_car.modal)

'''

# class Car:
#     def __init__(self, brand,modal):
#         self.brand=brand
#         self.modal=modal
#     def full_name(self):
#         return f"{self.brand} {self.modal}"
    
# my_car=Car("toyoya ","sift")
# print(my_car.brand)
# print(my_car.modal)
# print(my_car.full_name())


# my_new_car=Car("boloro","maruti")
# print(my_new_car.brand)
# print(my_new_car.modal)


# inharitence 
# class Car:
#     def __init__(self, brand,modal):
#         self.brand=brand
#         self.modal=modal
#     def full_name(self):
#         return f"{self.brand} {self.modal}"
# class ElectricCar(Car):
#     def __init__(self,brand,modal,betri_size):
#         super().__init__(brand,modal)
#         self.betri_size=betri_size
        
        
# my_tesla = ElectricCar("tesla","modal s ", "85kh")
# print(my_tesla.betri_size)
# print(my_tesla.brand)
# print(my_tesla.modal)
# print(my_tesla.full_name())


# class Student:
#     def __init__(self,name,father):
#         self.name=name
#         self.father=father
        
# # brajesh=Student("Brajesh mewada","Tulsiram ji mewada")
# # print(brajesh.name)
# # print(brajesh.father)
    
# himany=Student("Himany biitthe","Mr Ramesh ji")
# print(himany.father)
# print(himany.name)
        

# class Bank:
#     def __init__(self,Name,AcNumber):
#         self.name=Name
#         self.acnumber=AcNumber

# brajesh=Bank("Ram",901910110002788)
# print(brajesh.name)
# print(brajesh.acnumber)


# class Student:
#     def __init__(self,name,lastname):
#         self.name=name
#         self.last=lastname
    
#     def full_name(self):
#         return f"{self.name} {self.last}"

# brajesh=Student("Brajesh","mewada")
# print(brajesh.full_name())



class Car:
    def __init__(self, brand,modal):
        self.brand=brand
        self.modal=modal
    def get_brand(self):
        return

my_car=Car("toyoya ","sift")
print(my_car.brand)
print(my_car.modal)

my_new_car=Car("boloro","maruti")
print(my_new_car.brand)
print(my_new_car.modal)
