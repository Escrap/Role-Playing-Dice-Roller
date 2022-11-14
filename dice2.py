import random

rolling = True

while rolling:
    
    total = 0
    try:
        rolls = int(input("How many dice to roll? "))
    except:
        ValueError
        print("Rolls must be a number: Kindly Retry")
        continue
    
    try:
        sides = int(input("How many sides does die have? "))
    except:
        ValueError
        print("Sides must be a number: Kindly Retry")
        continue

    
    for die in range(rolls):
        roll = random.randint(1,sides)
        total += roll
        print(die+1,"Rolled: ", roll)                             #Add in "rolled: " and see what happens? could not reproduce error of score on each line
    print("score: ", total, "\n")
    

    roll_again = input("Roll again? (Y/N) ")
    if roll_again.upper() == "N":
        break

    print("n")