d1={
    "name":"sri kant kumar",
    "age":19,
    "cgpa":{"s1":7.9,"s2":7.9,"s3":7.4}
}
d2 ={}
# key is immutable value is mutable
# keys should be unique
print(d1["name"])
print(d1["age"])
print(d1.get('name'))
print(d1["cgpa"]["s3"])
d1["age"] =20
d1["college"] ="Gec siwan"
print(d1)
d1["cgpa"]["s4"]=7.5
print(d1)

del d2
del d1["age"]
print(d1)
# d1.clear()
print(d1)

for i in d1:
    print(i,d1[i],sep=" : ",end="\n")

print("name" in d1)
print("sri kant" in d1)
print(d1.keys())
print(d1.values())
