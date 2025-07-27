password = "admin123"
chance = 0

while chance <3 :
    guess = input("enter the password: ")
    if guess  == password:
        print("login successfull")
        break
    else:
        if chance >= 2:
           print("too many attempts")
           break
        else: 
           print(" incorrect try again")
           chance = chance + 1
           
           
    
    
    

    

