# Number gyessing game 
def checktry(num_u,num_com):
    user_input=num_u
    computer_input=num_com
    if int(user_input)<0 or int(user_input)>7:
        print("please guess in range of 1 to 7")
    else:
       if int(user_input)-int(computer_input)>0:
           print("you guessed more than me")
   
       elif (int(user_input)-int(computer_input)<0):
           print("you guesed less than me")
       else:
           print("you guessed right and you win")
           exit()
print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 7")
print("Can you guess what it is?")
print("you have seven attempts only:")
import random as rn
computer_guess=rn.randint(1,10)
user_attempt=7
while((user_attempt-1)!=0):
    user_input=input("Enter Your  Guess")

    print("you have ",user_attempt-1," attempt left")
    checktry(user_input,user_input)
    user_attempt=user_attempt-1
