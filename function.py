def is_even(a):
    "'this code check if it is true or false'"
    if(type(a)==int):
        return f"{a} is Even" if(a%2==0) else f"{a} is Odd"
    else:
        return "enter valid integer"

print(is_even.__doc__)
for i in range(11):
    print(is_even(i))

print(is_even("hello"))


def multiply(a=1,b=1):
    return a*b

def power(b =1,a =1):
    return a**b

def total_sum(*a):
    sum =0
    for i in a:
        sum+=i
    return sum

print(total_sum(1,2,2,3,3,4,5,6))

def a():
    def b(x,y):
        return x*y
    return b

print(a()(2,3))
