# from functools import reduce


# lambda jiska koe name nahi hota he 
# sntex 
# lambda (argument): Exception 
# esa function jo maltipal expresan lekar return kare  multipal output
    
    
x=lambda name : print("heelo",name)
x ("brajesh")


x=lambda x,y: x+y
print(x(10,20))

x=lambda x,y: x+y
p=int(input("enter fist number"))
q=int(input("enter secend number"))
print(x(p,q))



x=lambda name : print("heelo",name)
y=input("enter your anme")
x(y)


my_list=[10,20,30,40,50]
x=list(map(lambda x: x**2,my_list))
print(x)


#  even number
my_list=[10,20,30,40,50,43,23]
x=list(filter(lambda x: x%2==0 ,my_list))
print(x)


# odd number
# my_list=[10,20,30,40,50,43,23]
# x=list(filter(lambda x: x%2==1 ,my_list))
# print(x)

from functools import reduce
# my_list=[10,20,30,40,50,43,23]
# def max(x,y):
#     if x>y:
#         return x
#     else:
#         return y
# x= reduce(max,my_list)
# print(x)


my_list=[10,20,30,40,50,43,23]
def max(x,y):
    if x<y:
        return x
    else:
        return y
x= reduce(max,my_list)
print(x)


my_list=[10,20,30,40,50,43,23]
def max(x,y):
    return x+y
x= reduce(max,my_list)
print(x)



# reduce function ka use ham collation me se 1 obj return karna ho too reduce ka use karte he

my_list=[10,21,123,1233,14]
def max(x,y):
    if x>y:
        return x
    else:
        return y
x=reduce(max,my_list)
print(x)



my_list=[10,21,123,1233,14]
def max(x,y):
    if x<y:
        return x
    else:
        return y
x=reduce(max,my_list)
print(x)



my_list=[10,21,123,1233,14]
def max(x,y):
    if x+y:
        return x+y
    # else:
    #     return y
x=reduce(max,my_list)
print(x)


x=int(input("enter any number"))
def factorilal (x):
    return 1 if (x==1) or (x==0) else x
print(factorilal)


x = lambda a, b, c: a + b + c
print(x(5, 6, 2))



def myfunc(n):
  return lambda a : a * n
mydoubler = myfunc(2)
print(mydoubler(11))