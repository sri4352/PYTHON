import sys
# memory addressing
a =4
adress =id(a)
hex_adress =hex(adress)

val_adress =id(4)
hex_val_adress =hex(val_adress)
print(adress)
print(val_adress)
print(hex_adress)
print(hex_val_adress)

# aliasing
a =4
b =a
c =b
print(id(a))
print(id(b))
print(id(c))

del a
print(b)

a =5
b =a
a =6
print(b)

a ="apple"
b =a
c =b
print(sys.getrefcount(a))


#garbage collection
a =5
b =a
c =b
del a
del b
del c

#weired staff

a =2
b =a
c =a
print(sys.getrefcount(a))

a =257
b =257
print(id(a))
print(id(b))
#-5 to 256

a ="hello"
b ="hello"
print(id(a))
print(id(b))

a ="hello world"
b ="hello world"
print(id(a))
print(id(b))

a ="hello_world"
b ="hello_world"
print(id(a))
print(id(b))

a =[1,2,3]
b =a
b.append(5)
print(a)

a =[1,2,3]
b =a[:]

