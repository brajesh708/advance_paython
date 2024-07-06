#  this is a create file program
# f=(open('new','x'))
# print("file crate succsesfully")


# this is a write line program
# f=(open('new','w'))
# f.write("this is new file")
# print("file data add succsesfully")



#this is a read line program
f=(open('new','r'))
print(f.read(10))
print(f.closed)
f.close()
print(f.mode)






