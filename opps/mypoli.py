# print("this is  a new car")
# print(4+9)
# print("ewz,z")

# if any function retpiti  more time this is polimarshim

# class Vip:
#     def raj(self,x=None,y=None):
#         if x==None and y==None:
#             print("thanks for visiting this site")
#         elif x!=None:
#             for i in range(1,x+1):
#                 f=x*i
#             print(f)
#         else:
#             print("adition of numbers =",x+y)
# obj=Vip()
# # obj.raj()  
# obj.raj(5)      
# obj.raj(10,12)

# methode overriding 
# class A:
#     def raj(self):
#         print("hi")
# class B(A):
#     def raj(self):
#         print("hello")
#     def xyz(self):
#         print("tata")
#         super().raj()
# obj=B()
# obj.raj()
# obj.xyz()



# oprator overloding( )
class A:
    def raj(self ,x):
        self.x=x
        
obj=A()
obj.raj(10)