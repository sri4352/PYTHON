name ="sri kant kumar"
name ='sri kant kumar'
name ="'sri kant kumar'"
name ='''sri kant kumar'''
name =str("sri kant kumar")

print(name)
print(name[5])
print(name[-3])

print(name[2:6])
print(name[4:])
print(name[:])
print(name[2::2])
print(name[-7:-2])
print(name[-2:-9:-2])
print(name[::-1])

# name[0] ='k' cannot perform bacause string is immutable

name ="s kumar" #can be reassign

name ="sri kant kumar"
temp ="s kumar"
del temp
print(temp)

#operations
a ="hello"
b =" world"
c =a+b
print(c)
print(c*4)
print("mumbai"<'pune') #lexographucaally comparison
print(a<b)
print("sri"<"Sri")

print("" and a)
print("" or a)
print(a and b)
print(a or b)
print(not a)
print(not "")

for i in  c:
    print(i,end="")

print()
for i in c[1::3]:
    print(i,end="")

print()

print("e" in c)
print('c' in c)

#function

print(len(c))
print(max(c))
print(min(c))
list =sorted(c,reverse="false")
print(list)
print(sorted(c))

print(reversed(c))

print(c.upper())
print(c.lower())
print(c.title())
print(c.swapcase())

print(c.count('o'))
print(c.index('e'))
print(c.find('x'))
print(c.startswith('w'))
print(c.startswith('w',6))

sentence ='my name is {} and i am studying {}'.format("sri kant kumar","cse")
print(sentence)
sentence ='my name is {1} and i am studying {0}'.format("cse","sri kant kumar")
sentence ='my name is {name} and i am studying {study}'.format(study="cse",name ="sri kant kumar")
print(sentence)

temp ="sri430$"
print(temp.isalnum())
print(temp.isalpha())
temp ="20"
print(temp.isdigit())
print(temp.isidentifier())


sentence ="who is the pm of india"
list =sentence.split()
print(list)
list =sentence.split("i",2)
print(list)

join_string ="i".join(list)
print(join_string)
sentence =sentence.replace("india","america")
print(sentence)

sentence ="     this is pm       of india          "
sentence =sentence.strip()
print(sentence)

