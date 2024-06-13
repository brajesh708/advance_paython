

# def squar(num):
#     for i in range (1,num+1):
#         print(i*i)
# squar(10)

#  genretor funtion 
# yield keword return ke place par use hota he 

# def squar(num):
#     for i in range (1,num+1):
#         yield i*i
# data=squar(10)
# for i in data :
#     print(i)


# num=int(input("enter any number"))
# if num/2==0:
#     return 



# for i in  range (2,20,2):
#     print(i)

# def squr(num):
#  for i in  range (2,num,2):
#     return i
# data=squr(20)
# print(data)



num = int(input("Enter a number: "))

# initialize sum
sum = 0

# find the sum of the cube of each digit
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")


