l =[]
l =[1,2,3,4,5]
l =[2,3.4,False,'sri',5+6j]

l =[1,2,3,[4,5]]
l =[[[1,2],[3,4],[5,6]]]
l =list("sri kant")
l =list()

l  =[1,2,3,4,5]
print(l[0])
print(l[-4])
print(l[1:5])
print(l[::-1])

l =[1,2,3,[4,5,6]]
print(l[-1][2])

l[0] =100
print(l)
l[-3] =20
print(l)
l[0:3] =[100,200,300]
print(l)

list =[1,2,3,4,5]
list.append(200)
print(list)
list.extend([40,50,60])
list.append([20,50,70])
print(list)
list.insert(2,"world")
print(list)
list.insert(3,[10,40,56])
print(list)

del list[0]
print(list)
del list[-3:-1]
print(list)
list.remove(3)
print(list)
list.pop()
print(list)
list.clear()
print(list)

list =[1,2,3,[4,5],10,20]
list =l+list
print(list)
print(list*3)

for i in list:
    print(i,end=" ")

print()
for i in list[-3:-1]:
    print(i)

print(4 in l)

list =[3,5,6,7,1,2,9]
print(len(list))
print(max(list))
print(min(list))
print(sorted(list))
print(sorted(list,reverse=True))
list.sort()
print(list)
print(list.index(3))

