import random
input_no =int(input("enter no :"))
count =1
guess_no =random.randint(1,10)
while(input_no!=guess_no):
    if(input_no>guess_no):
        print("enter less no")
    elif(input_no<guess_no):
        print("enter high value")
    input_no =int(input("enter no :"))
    count+=1

print("guess correct no in ",count,"attempts")
