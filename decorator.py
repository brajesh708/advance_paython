#  function ke andar new fansanality lana decorater hota  he




def Student():
    print("this is a orignal ")
    
def decorator(fun):
    def wrapper():
        print("start work")
        fun()
        print("stop work")
    return wrapper
var=decorator(Student)
var()
    
    
    
    

    
# def decorator(fun):
#     def wrapper():
#         print("start work")
#         fun()
#         print("stop work")
#     return wrapper
# @decorator
# def Student():
#     print("this is a orignal ")
# Student()



    
def decorator(fun):
    def wraper():
        print("start work")
        fun()
        print("stop work")
    return wraper
@decorator
def Student():
    print("this is a orignal ")
Student()