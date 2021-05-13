import random
user_choice=input("Please enter: rock paper or scissor-- ")
print("Your choice-",user_choice)

x=["rock","paper","scissor"]
computer_choice=random.choice(x)
print("Computer's choice-",computer_choice)


if user_choice==computer_choice:
    print("The game is Draw")

elif user_choice=="rock" and computer_choice=="paper":
    print("Computer won this round")

elif user_choice=="paper" and computer_choice=="rock":
    print("You won this round")
elif user_choice=="paper" and computer_choice=="scissor":
    print("Computer won this round")
elif user_choice=="scisssor" and computer_choice=="paper":
    print("You won this round")
elif user_choice=="scissor" and computer_choice=="rock":
    print("Computer won this round")
elif user_choice=="rock" and computer_choice=="scissor":
    print("You won this round")
else:
    print("Invalid choice")