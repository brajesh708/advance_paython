# inheretians  3 type ke hote he
# 1 singal level inheritece ex= perent ---child
#  2 maltilevel inheritance ex = grend father ---father---son
# 3 multipale inheritance  ex = father ---mother dono ki propaty ---son ko mil jaye too
#  nana ji ki property mammy ko or dada ji ki property papa ko dono apne ko mil jaye to multipale inhetitance hota he 

# singal 
# class A:
#     name="brajesh"
#     def m1(self):
#         return "this is m1 methode "
        
# class B(A):
#     def m2(self):
#         print("name =",A.name)
#         print("m1=",self.m1())
# obj=B()
# obj.m2()



# maltilevel

# class A:
#     name="brajesh"
#     def m1(self):
#         return "this is m1 methode "
        
# class B(A):
#     age=22
#     def m2(self):
        
#         print("name =",A.name)
#         print("m1=",self.m1())
# class C(B):
#     def m3(self):
#         print("age=",B.age)
#         self.m2()
# obj=C()
# obj.m3()

# maltipal


# class Parent1:
#     def m1(self):
#         print("m1 methode callad")
# class Parenet2:
#     def m1(self):
#      print("me methode is calld")
# class Child(Parenet2,Parent1): # mro ke anusar jo pehele likhenge bo pehle print hoga
#     def m3(self):
#         self.m1()
# obj=Child()
# obj.m3()



# class Parent1:
#     def m1(self):
#         print("m1 methode callad")
# class Parenet2:
#     def m1(self):
#         print("m ka  methode callad")
#     def m2(self):
#      print("me methode is calld")
# class Child(Parenet2,Parent1): 
#     def m3(self):
#         self.m1()
#         self.m2()
# obj=Child()
# obj.m3()



#  overright methode 
# class A:
#     def m1(self):
#         print("m1 called from A")
# class B(A):
#     def m1(self):
#         print("m1 clald is B")
#         super().m1()   # uper ki class ka data print karne ke liye 
# obj=B()
# obj.m1()

