#  kisi bhi progaming knowledge  me real word antties ko program me aad karne ka liye oops ka use karte he

# class object 

#  example mobolie  color ,body,buuton



# without constractor   ----class ko coll kiya 
# class Student:
#     stu_qualification="M.tech"
#     def stu_detail(name,age):
#        print("stuname",name)
#        print("stuage",age)
#        print("qualification",Student.stu_qualification)
       
# obj=Student
# obj.stu_detail("brajesh",20)




#  with constractor classs ko coll 
#  __init__ ek constaktor he ese megic funtion or dindar or specal constrotor bhi kahete he yaha outometic  coll hota he 
# class Student:
#     qualifiaction="B.Teach"
#     def __init__ (self):
#         print("constactor colled")
        
# obj=Student()
# print(obj)
    
    
    # dir se sabhi option aate he
    
# class Student:
#     qualifaication="m.tech"
#     def stu_detels(self,same,age):
#         print("name =",same)
#         print("age =" , age)
#         print("qualification",Student.qualifaication)
# obj=Student()

# obj.stu_detels("brajesh",22)


# vaiable  3 type ke hote he

# 1 instance variable jo ojct badalne ke sath me value badal de instance variable hota  he
#  jo na badle bo static variable
# local ka use methode ke ander karte he

# class Student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def display(self):
#         print(self.name)
#         print(self.age)
# obj=Student("brajesh",22)
# obj.display()
# print(obj.name)
# print(dir(obj))
# #  dir se method fin hoti he
# print(obj.age)
# obj2=Student("raj",12)
# print(obj2.name)
# print(obj2.age)


 
#     most importent self 
#  self is a reference variale of currunt object of current class 


# class Student:
#     Qualifilation="M.tech"  #static variavle jo kabhi na badle 
#     def __init__(self,name):
#         self.name=name     # instence variable   jo obj ke sath badle
#     def display(self):
#         age=37              # local variable    jo function ke ander hi coll ho
#         print("name",self.name)
#         print("age",age)
#         print("qualification",Student.Qualifilation)
# obj=Student("brajesh")
# obj.display() 



# how we declear instance veriable
#  1 through constractor 
#  2 though instance methode 
#  3  though object 




#  using instance method
# class Student:
#     def display(self,name):
#        self.name=name
#     def show(self):
#         print("name",self.name)
# obj=Student()
# obj.display("brajesh")
# obj.show()


#  3  using though object 
# class Student:
#     def __init__(self,name):
#         self.name=name      # though constractor 
#     def display(self,age):
#         self.age=age     # though instance methode
        
#     def show(self):
#         print('name',self.name)
#         print('age',self.age)
#         print('quali',self.quali)
        
# obj=Student('brajesh')
# obj.display(37)
# obj.quali='B tech'    #using though out object methode 
# obj.show()


#  how we access instance variable
# 1 inside the class   === self ki help se
# 2 out side the class === object ki help se
# ----------------------------------------------------------------------

# #                    static variable === jo kabhi na badle 
# class Student:
#     quali = "M.Tech"   # static variable declare inside the class   
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         Student.school = "SHSS"  # static variable declare inside the constructor
#     def display(self):
#         Student.gread = "P.hd"   # static variable declare inside the instence variable
#         print("Name = ",self.name)
#         print("Age = ",self.age)
#         print("Quali =",Student.quali)  # static variable access inside the class through class name
#         print("School = ",Student.school) # static variable access inside the class through class name
#         print("Gread = ",Student.gread) # static variable access inside the class through class name
#         print("Achivment = ",Student.achivment)   # static variable access inside the class through class name

# obj = Student("Neeraj",37)
# Student.achivment="Gate-qualified"   # static variable declare outside of the class
# print("Access through class_Name = ",Student.quali) # static variable access outside the class through class name
# print("Access through object = ",obj.quali) # static variable access outside the class through object
# obj.display()
# print("Access through class_Name = ",Student.gread) # static variable access outside the class through class name
# print("Access through class_Name = ",Student.school)# static variable access outside the class through class name
# print("Access through class_Name = ",Student.achivment)# static variable access outside the class through class name
# #  obj.display()




# class Student:
#     def display(self)
#     global a
#     a=10
#     print ("value of a ",a)
    








    
    