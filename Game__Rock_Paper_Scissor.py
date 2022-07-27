import random
import git

def gameRPS(comp, you):
    # If two values are equal. Declare a tie!
    if comp == you:
        return None
    #Check for other possibilities when computer choose rock.
    elif comp == 'rock':
        if you == 'paper':
            return True
        elif you == 'scissor':
            return False
    # Check for other possibilities when computer choose paper.
    elif comp == 'paper':
        if you == 'rock':
            return False
        elif you == 'scissor':
            return True
    # Check for other possibilities when computer choose scissor.
    elif comp == 'scissor':
        if you == 'rock':
            return True
        elif you == 'paper':
            return False

print("computer turn: rock(r), paper(p) or scissor(s)")
x = random.randint(1,3)
if x == 1:
    comp = "rock"
elif x == 2:
    comp = "paper"
elif x == 3:
    comp = "scissor"

you = input("your turn: Choose rock(r), paper(p) and scissor(s):\t")

y = gameRPS(comp, you)

print(f"Computer choose: {comp}")
print(f"You choose: {you}")
if y == None:
    print("It's a tie. Better luck next time")
elif y == True:
    print("Congrats! You Win")
else:
    print("Sorry! You loose")

