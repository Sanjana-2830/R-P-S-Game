import random
item_list =["rock","paper","scissor"]

user_choice = input("Enter User Move = Rock,Paper,Scissor = ")
computer_choice = random.choice(item_list)

print(f"User Choice = {user_choice} and computer_choice = {computer_choice}")

if computer_choice == user_choice:
    print("Match Tie")
elif computer_choice == "rock" and user_choice == "scissor" :
    print("computer wins")
elif computer_choice == "rock" and user_choice == "paper":
    print("User Wins")
elif computer_choice == "paper" and user_choice =="rock" :
    print("computer wins")
elif computer_choice == "paper" and user_choice == "scissor":
    print("user wins")
elif computer_choice == "scissor" and user_choice == "rock":
    print("user wins")
elif computer_choice == "scissor" and user_choice == "paper":
    print("computer wins")

