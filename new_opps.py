# class Car:
#     def __init__(self,brand,modal):
#         self.brand=brand
#         self.modal=modal
        
        
    
# my_car=Car(2023,"thar")
# print(my_car.modal)
# print(my_car.brand)


# my_new_car=Car(2020,"boloro")
# print(my_new_car.modal)


# class Car:
#     def __init__(self,brand,modal):
#         self.brand=brand
#         self.modal=modal
        
#     def full_name(self):
#         return f"{self.brand} {self.modal}"
    
# my_car=Car(2023,"thar")
# print(my_car.modal)
# print(my_car.brand)
# print(my_car.full_name())


# my_new_car=Car(2020,"boloro")
# print(my_new_car.modal)





# class Car:
#     def __init__(self,brand,modal):
#         self.brand=brand
#         self.modal=modal
        
#     def full_name(self):
#         return f"{self.brand} {self.modal}"
    
# class Electric(Car):
#     def __init__(self,beetrisize,brand,modal):
#         super().__init__(brand,modal)
#         self.betrisize=beetrisize
        
    

# print

# my_new_car=Car(2020,"boloro")
# print(my_new_car.modal)

class Vip:
    def a(self,x=None,y=None):
        if x==None and y==None:
            print("thanku for visit")
        elif x!=None:
            for i in range(1,x+1):
                f=f*1
            print(f)
        else:
            print("addtion of two numbers",x+y)
raj=Vip()


my_list=[33,33,56,90,89]
def even(n):
    if n%2==0:
        return 'even'
    else:
        return 'odd'
obj=map(even,my_list)
print(list(obj))