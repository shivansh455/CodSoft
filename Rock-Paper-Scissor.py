"""
Workflow of the project:
1-Input from user(Rock,paper,scissor)
2-Computer choice (Computer will choose randomly not conditionally)
3-Result Print

Cases:
A-Rock
Rock-Rock = tie
Rock-Paper = paper win
Rock-Scissor=Rock win

B-Paper
Paper-Paper=tie
Paper-Rock=Paper win
Paper-Scissor=Scissor win

C-Scissor
Scissor-Scissor=tie
Scissor-Rock=Rock win
Scissor-Paper=Scissor win

"""

import random
item_list=["Rock","Paper","Scissor"]
user_choice=str(input("Enter your move = Rock,Paper,Scissor ="))
comp_choice=random.choice(item_list)

print(f"user choice = {user_choice}, Computer Choice ={comp_choice}")

if user_choice == comp_choice:
    print("Both Chooses Same : Match Tie")
elif user_choice == "Rock":
    if comp_choice == "Paper":
        print("Paper Covers Rock : Computer win")
    else:
        print("Rock Smashes Scissor : You win")
elif user_choice == "Paper":
    if comp_choice == "Scissor":
        print("Scissor cuts paper : Computer win")
    else:
        print("Paper Covers Rock : You win")

elif user_choice == "Scissor":
    if comp_choice == "Paper":
        print("Scissor cuts paper : You win")

    else:
        print("Rock Smashes Scissor : Computer win")
