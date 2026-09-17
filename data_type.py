#Basic

#integer
print(23)
print(-23)
print(1e309) #range

#float
print(4.5)
print(-2.4)
print(1.7e309)#range

#boolean
print(True)
print(False)

#complex
print(4+5j)

#string
print('sri kant')
print("sri kant")
print("""sri kant kumar""")


#container

#list
print([1,2,3,4,5])

#tuple
print((1,2,3,4,5))

#set
print({1,2,3,4,5})

#dictionary
student ={
        "name" :"sri kant kumar",
        'age':19,
        'gender':"male"
}
print(student["age"])

#user defined

#class
class person:
    def __init__(self,name,age):
        self.name =name
        self.age =age
    def print_info(self):
        print("name :",self.name)
        print("age ",self.age)

