

num1=float(input("enter a number:"))
num2=float(input("enter another number:"))

operator=input("enter the operation -,+,/,*,%:")

if(operator=='-'):
    print(num1-num2)
elif operator == '/':
    if num2 != 0:
        print(num1 / num2)
    else:
        print("Cannot divide by zero!")
elif(operator=='*'):
    print(num1*num2)
elif(operator=='+'):
    print(num1+num2)
else:
    print("enter a valid stuffs dude")   

str="man"
try:
   print( x=int(str))
except:
    print("hey the try is not working"+""+str)

#Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.

#Enter Hours: 45
#Enter Rate: 10 

#Pay: 475.0

hours=float(input("enter the hours:"))
Rate=float(input("enter the Rate:"))

if(hours>40):
    rest=hours-40
    left=float(rest*1.5)
    score=40*Rate
    (print(score+left))
else:
    (print(hours*Rate))
