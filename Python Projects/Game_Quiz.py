print("Hello There! Welcome To The Cricket Quiz Game!")
playing=input('Wanna Play The Cricket Quiz? ')
if playing.lower() != 'yes':
    quit()
print("Great! Let Us Start Our Cricket Quiz :-)")
score=0
answer=input("How many centuries did Sachin Tendulkar scored in his cricket carrier ")
if answer.lower()=="100":
    print("Wow That Is Correct! Let Us Head Towards Another Question. ")
    score += 1
else:
    print("Ahhh! That IS Incorrect :(")
answer=input("Who is the most successfull captain in the history of test cricket ")
if answer.lower()=="steve waugh":
    print("Wow That Is Correct! Let Us Head Towards Another Question. ")
    score += 1
else:
    print("Ahhh! That IS Incorrect :(")
answer=input("Who is the most successfull captain in the history of One Day International cricket ")
if answer.lower()=="ms dhoni" or "mahendra singh dhoni" or "dhoni":
    print("Wow That Is Correct! Let Us Head Towards Another Question. ")
    score += 1
else:
    print("Ahhh! That IS Incorrect :(")
answer=input("Who is the most successfull captain in the history of T20 International cricket ")
if answer.lower()=="rohit sharma":
    print("Wow That Is Correct! Let Us Head Towards Another Question. ")
    score += 1
else:
    print("Ahhh! That IS Incorrect :(")
answer=input("Which is the most successfull cricket team in internatinal cricket")
if answer.lower()=="australia" or "australian cricket team":
    print("Wow That Is Correct! Let Us Head Towards Another Question. ")
    score += 1
else:
    print("Ahhh! That IS Incorrect :(")

print("Total Correct Answers Are" + str(score))
print("You Got" + str((score/5)*100) + "%" + "answers correct.")
print("Thank You For Playing The Quiz Game!")