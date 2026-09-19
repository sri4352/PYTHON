# while loop

n =int(input("enter no :"))
i =0
while(i<=10):
    print(n," X ",i,"=",n*i)
    i +=1

#for loop

temp =[]
for i in range(11):
    temp.append(i)
print(temp)

temp.clear()

for i in range(1,11):
     temp.append(i)
print(temp)
temp.clear()

for i in range(1,11,2):
     temp.append(i)
print(temp)
temp.clear()

for i in range(11,0,-2):
     temp.append(i)
print(temp)
temp.clear()

for i in "sri kant kumar":
     temp.append(i)
print(temp)
temp.clear()

list =[1,2,3,4,5]
for i in list:
     print(i)

#nested loop

n =int(input("enter no of rows :"))
for i in range(1,n+1):
    for j in range(i):
        print("*",end=" ")
    print(" ")

