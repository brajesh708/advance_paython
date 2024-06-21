#  file hendling me file 2 type ki
# text file 
# binary file esme idio or vidio or img rakte he


#  open()
# write /read/delet/edit 
# close() 


# new file creat
# p=open('h5.txt','x')
# print(p.mode)  
# print(p.closed)
# p.close()
# print(p.closed)

f=open('h5.txt','w')
print(f.mode)
print(f.closed)
f.close()
print(f.closed)

# f=open('h1.py','x')
# print(f.mode)


# new data likne ke liye 
# p=open('h5.txt','w')
# p.write('this is new')
# p.close()

# maltiple line ke  liye 
# p=open('h5.txt','w')
# data=("this  is my new data \n","my name is  brajesh \n", "go to ehore")
# p.writelines(data)
# print(p.writable())


#  read karne ke liye 
# p=open('h5.txt','r')
# print(p.mode)
# data=p.read()
# print(data)



# p=open('h5.txt','r')
# print(p.mode)
# data=p.read()
# print(data)
# p.read(10)
# p.close()


# p=open('h5.txt','a')
# p.write("\nHello to the world of python")
# p.close()

# p=open('h5.txt','a')
# p.write("\nHello to the world of python")
# p.close()


# p=open('h5.txt','r+')
# p.write("\nHello to the world of python")
# print(p.readable())
# p.close()



# tell ka use ham cursur point dekne ke liye karte he 
# p=open('h5.txt','r')
# print(p.tell())
# print(p.read(5))
# print(p.tell())
# print(p.read(10))
# print(p.tell())

# print(p.readline())
# print(p.tell())

# print(p.read())
# print(p.tell())
# print(p.read(5))




# seek ki requrmnet  jis index par ke ke jana ho baha par 
# p=open('h5.txt','r')
# print(p.tell())
# print(p.read(3))
# (p.seek(0))
# print(p.tell())
# print(p.read(10))
# print(p.tell())
# p.seek(15)
# print(p.tell())


#  baynary mode me 
# p=open('h5.txt','rb')
# print(p.tell())
# p.seek(-10,2)
# print(p.tell())
# print(p.read(10))


# p=open('h5.txt','rb')
# print(p.tell())
# p.seek(10,1)
# print(p.tell())
# print(p.read(10))



# p=open('h5.txt','rb')
# print(p.tell())
# print(p.read(12))
# p.seek(10,0)
# print(p.tell())
# print(p.read(10))
# p.close()



#  esa likhne se close nahi karna padta he
# with open('h5.txt','r')as p:
#     print(p.read(10))
#     print(p.tell())
#     p.seek(10)
#     print(p.tell())
#     print(p.closed)
# print(p.closed)
    
    
    
with open('h5.txt','rb')as p:
    print(p.read(10))
    print(p.tell())
    p.seek(10,1)
    print(p.tell())
    print(p.closed)
print(p.closed)
    








