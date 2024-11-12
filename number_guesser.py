import random
max_range = input("Type Any Number: ")
if max_range.isdigit():
    max_range=int(max_range)
    if max_range<=0:
        print("Please type a number greater than 0 next time.")
        quit()
else:
    print("Please type a number next time.")
    quit()
random_num=random.randint(0,max_range)
guesses=0
while True:
    guesses +=1
    guesses_by_user=input("Make a guess: ")
    if guesses_by_user.isdigit():
        guesses_by_user=int(guesses_by_user)
    else:
        print("Please type a number next time")
        continue
    if guesses_by_user == random_num :
        print("Correct Guess :)")
        break
    elif guesses_by_user < random_num:
        print("Guessed Number Is Below The Correct Guess")
    else:
        print("Guessed Number Is Above The Correct Guess")
print("You Got The Correct Number In", guesses, "Guesses")
