import random

print("enter rock as 1 , paper as 2 and scissor as 3")

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
elif (choice == 2 and computer_choice == 3) or (choice == 3 and computer_choice == 2):
    result = "Scissor"
elif (choice == 3 and computer_choice == 1) or (choice == 1 and computer_choice == 3):
    result = "Rock"

if choice == computer_choice:
  print("Draw")
elif result == choice:
  print("you win")
else:
  print("computer win")

print("done")



 
 

 




 
 