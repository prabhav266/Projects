import random
player_wins = 0
computer_wins = 0
options = ["rock","paper","scissors"]
while True:
    player_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if player_input == "q":
        break
    if player_input not in options:
        continue
    random_num = random.randint(0,2)
    computer_choice = options[random_num]
    print("computer chose", computer_choice +".")
    if player_input == "rock" and computer_choice == "scissors":
        print("Yayyy!You Won. :)")
        player_wins += 1
    elif player_input == "paper" and computer_choice == "rock":
        print("Yayyy!You Won. :)")
        player_wins += 1
    elif player_input == "scissors" and computer_choice == "paper":
        print("Yayyy!You Won. :)")
        player_wins += 1
    elif player_input == computer_choice:
        print("Woah! It Is A Tie. :)")
    else:
        print("You Lost. :(")
        computer_wins += 1
print("You Won", player_wins, "times.")
print("Computer Won", computer_wins, "times.")
print("GoodBye!")