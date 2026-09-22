t1 =()
t2 =(1,2,3,4,5)
t3 =(True,"sri",2,3.4)
t4 =(t1,t2,t3)
t5 =(t4,t2)
t6 =(1,)
t6 =("hello",)
t7 =tuple("hello")

print(t2[1])
print(t2[-2])
print(t2[2:5])
print(t4[1][2])

# t2[1] =100 tuples is immutable

print(t2*4)
t8 =t2*5
print(t8)
t8 =t2+t3+t4
print(t8)

for i in t8:
    print(i,end=" ")

print()
print(2 in t8)
print(len(t8))
print(min(t2))
print(min(t2))
print(sum(t2))
print(sorted(t2,reverse=True))

# tuples is read only data type

