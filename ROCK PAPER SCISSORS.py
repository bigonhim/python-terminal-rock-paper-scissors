#This project clearly defines how a rock paper scissors game can be played with a computer in python code
import random
user_wins=0
computer_wins=0

choices=["rock","paper","scissors"]
while True:
    user_input =input("Please choose between rock/paper/scissors or Q to quit: ").lower()
    if user_input == "q":
       break
    if user_input not in choices:
     print("Wrong input \n please try again")
     continue
    import random
    random = random.randint (0,2)
    computer_input=choices[random]
    print("The computer picked " + computer_input) 

    if user_input =='rock' and computer_input =="scissors":
       print ("YOU WON!")
       user_wins+=1
    elif user_input =='scissors' and computer_input =="paper":
       print ("YOU WON!")
       user_wins+=1       
    elif user_input =='paper' and computer_input =="rock":
       print ("YOU WON!")
       user_wins+=1
    else:
       print("COMPUTER WINS!")
       computer_wins+=1
              

print("You won",user_wins, "times")
print("The Computer won " ,computer_wins, "times")
if user_wins > computer_wins:
   print("YOU ARE THE OVERALL WINNER")
else:
   print("THE COMPUTER TAKES THE CREDIT")
print("GOODBYE!")
