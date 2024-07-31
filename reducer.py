import functools
my_list=[10,20,40,34,45,50]



from functools import reduce
my_list=[10,20,30,40,50,43,23]
def max(x,y):
    if x>y:
        return x
    else:
        return y
x= reduce(max,my_list)
print(x)


from functools import reduce
my_list=[10,20,30,40,50,43,23]
def min(x,y):
    if x<y:
        return x
    else:
        return y
mini=reduce(min,my_list)
print(mini)