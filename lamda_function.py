import functools 
sqr =lambda a:a*a
print(sqr(8))

check =lambda s: s[0]=='a'
print(check('apple'))

even_odd =lambda n:"even" if(n%2==0) else "odd"
print(even_odd(5))


def result_sum(func,List):
    result =0
    for i in List:
        if func(i):
            result =result+i
    return result

x =lambda x:(x%2==0)
y =lambda x:(x%2!=0)
z =lambda x:(x%3==0)

List =[11,14,21,23,56,78,45,29,28]
print(result_sum(x,List))
print(result_sum(y,List))
print(result_sum(z,List))

#map,filter and reduce

new_List =list(map(lambda x:"even" if x%2==0 else "odd",List))
print(new_List)

two_times =lambda x:x*2
List =list(map(two_times,List))
print(List)

students =[
    {
        "name":"sri kant kumar",
        "branch":"cse"
    }
    ,{
        "name":"sri",
        "brach":"civil"
    }
    ,{
        "name":"kant",
        "brach":"ee"
    }
]
extrct_name =lambda x:x["name"]
new_data =list(map(extrct_name,students))
print(new_data)

fruits =["apple","mango","orange","litchi","papaya"]
extrct_fruit =lambda x:'e' in x
new_fruits =list(map(extrct_fruit,fruits))
print(new_fruits)

fruits =["apple","mango","orange","litchi","papaya"]
extrct_fruit =lambda x:'e' in x
new_fruits =list(filter(extrct_fruit,fruits))
print(new_fruits)

sum =lambda x,y:x+y
total_sum =functools.reduce(sum,List)
print(total_sum)

greater_check =lambda x,y:x if(x>y) else y
max =functools.reduce(greater_check,List)
print(max)

smaller_check =lambda x,y:x if(x<y) else y
min =functools.reduce(smaller_check,List)
print(min)

# list comrehension

a =[1,3,4,5,7,8]
b =[i*2 for i in a]
print(b)

b =[i**2 for i in range(1,11)]
print(b)

b =[i**2 for i in range(1,11) if i%2!=0]
print(b)

b =[i**2 if i%2 ==0 else i for i in range(1,11)]
print(b)


students ={
    1:{
        "name":"sri kant kumar",
        "branch":"cse"
    },
    2:{
        "name":"sri",
        "branch":"civil"
    }
    ,3:{
         "name":"kant",
        "branch":"ee"
    }
}

for key,value in students.items():
    print(key,students[key]["name"],students[key]["branch"])

for key,value in students.items():
    print(key,value["name"],value["branch"])

# dictionary comprehension
new_dict ={
    key:value
    for key,value in students.items() if(len(value["name"])>3)
}

print(new_dict)
