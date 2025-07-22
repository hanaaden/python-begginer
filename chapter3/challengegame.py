import random

print("enter rock as 1 , paper as 2 and scissor as 3")
count = 1
computer1 = 0
person1 = 0
while(count>0):
  
  choice = int(input("enter a choice:"))

  if choice == 1:
   choice_game = "rock"
  elif choice == 2:
   choice_game = "paper"
  elif choice == 3:
   choice_game = "scissor"
  else: 
   print("invalid")

  print(choice_game)
  print("now it is computer time")

  computer_choice = random.randint(1,3)
  if computer_choice == 1:
   computerchoice_game = "rock"
  elif computer_choice == 2:
   computerchoice_game = "paper"
  elif computer_choice == 3:
   computerchoice_game ="scissor"
  else: 
   print("invalid")

  print(computerchoice_game)

  if choice == computer_choice:
    result = "Draw"
  elif (choice == 1 and computer_choice == 2) or (choice == 2 and computer_choice == 1):
    result = "Paper"
    print("the result was" , result)
  elif (choice == 2 and computer_choice == 3) or (choice == 3 and computer_choice == 2):
    result = "Scissor"
    print("the result was" , result)
  elif (choice == 3 and computer_choice == 1) or (choice == 1 and computer_choice == 3):
    result = "Rock"
    print("the result was" , result)
    
  if result == "Rock":
    scorer = 1
    print("the scorer was:" , scorer)
  elif result == "Paper":
    scorer = 2
    print("the scorer was:" , scorer)
  elif result == "Scissor":
    scorer = 3
    print("the scorer was:" , scorer)
    
  print("your choice was" , choice)

  if choice == computer_choice:
   print("Draw")
   print("computer score :" , computer1 , "your score :" , person1)
  elif choice == scorer:
   person1 = person1 + 1
   print("computer score :" , computer1 , "your score :" , person1)
   print("you win")
  else:
   computer1 = computer1 +1 
   print("computer score :" , computer1 , "your score :" , person1)
   print("computer win")

  print("done")
  count = count +1



 
 

 




 
 