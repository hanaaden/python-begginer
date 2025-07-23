#POAITIONAL PARAMETERS
def add(a, b):
    return a + b
print(add(3, 5))  # Output: 8
# Keyword Arguments:
def ad(a,b):
  print(ad(b=5, a=3))  # Output: 8
#Default Arguments:
def greet(name="Guest"):
    print(f"Hello, {name}!")
greet()  # Output: Hello, Guest!
# arbitrary argumetn 
def summarize(*args):
    return sum(args)
print(summarize(1, 2, 3, 4))  # Output: 10


def thing():
    print("I will tell you a joke")
    name= input("tell me you name=")
    print("no not in mood dude")
    print("sorry"+" "+name+" "+"no joke is here hahah dont call me again")
    
answer=str(input("do you wanna hear jokes:Y/N="))
if answer== 'y' or answer=='y':
    thing()

elif answer=='n' or answer=='N':
    print("chio")
else:
    print("invalid")
    
# parameter

def addtwo (a,b):
    added= a+b
    return added

x= addtwo(3,5)
print(x)

#exercise

def payment():
    hours= float(input("enter the hours:"))
    Rate= float(input("enter the Rate:"))
    if (hours>40):
       rest= hours-40
       left= float(rest*1.5)
       score= 40*Rate
       (print(score+left))
    else:
      (print(hours*Rate))
      
payment()