def multply(a,b):
    if(b==1):
        return a
    else:
       return a+multply(a,b-1)

print(multply(2,5))


def factorial(n):
    if n==1:return 1
    else:
        return n*factorial(n-1)

print(factorial(5))

def check_palindrome(s):
    if(len(s)<=1):return "palindrome"
    else:
        if(s[0]==s[-1]):
            return check_palindrome(s[1:-1])
        else :
            return "not palindrome"

print(check_palindrome("python"))
print(check_palindrome("madam"))

def fibonnic(n):
    if(n==0 or n==1):return 1
    else :
        return fibonnic(n-1)+fibonnic(n-2)

print(fibonnic(6))
