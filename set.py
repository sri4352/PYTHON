#no indexing no duplicates no mutable data type allowed
#set is also mutable
s1 ={} #this is dictionary
s1 =set()
s2 ={1,2,3,4}
s3 ={"hello",True,5.4}

# s4 ={[1,2,3],"hello"} not allowed
s5 ={"hello",(1,2,3,4,5),2,3.5}
print(s5)

s6 ={1,2,3,4,5}
print(id(s6))
l =list(s6)
l[1] =100
s6 =set(l)
print(s6)
print(id(s6))
#both are different

s6.add("sri")
print(s6)

del s2
s6.remove(3)
s6.pop()
print(s6)

s1 ={1,2,3,4,5}
s2 ={3,4,5,6}
for i in s1:
    print(i,end=" ")

print(len(s1))
print(min(s1))
print(max(s1))
print(sum(s1))
s1 =sorted(s1,reverse=True)

print(s1)
s1 =set(s1)
s1 =s1.union(s2)
print(s1)
s1 =s1.intersection(s2)
print(s1)
s1 =s1.difference(s2)
print(s1)
s1.difference_update(s2)
print(s1)
s1 ={1,2,3,4,5}
s1 =s1.symmetric_difference(s2)
print(s1)
print(s1.isdisjoint(s2))
print(s1.issubset(s2))
print(s1.issuperset(s2))
