ask = int(input("what is you age: "))
if ask >= 21:
    print("you can vote,drive and drink")
elif ask >= 18 :
    print("you can drive and vote")
elif ask >= 16:
    print("you can drive only")
else:
    print("you cannot vote drink or drive")
    
asj1 = int(input("enter a number: "))
try:
    if asj1 == " ":
     print("enter valid number")
    else:
      if asj1%2==0:
       print("it is even number")
      else:
       print("it is odd number")
except:
    print("unknown error please refresh")