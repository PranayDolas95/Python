import random
i = random.randint(0,9)
print(i)

tries = 1 
points = 100
while(tries <=3):
    j = int(input("Guess the number : "))

    if(j == i):
        print("You have Won and you scored ", points, " points in", tries, "tries.")
        break 
        if(points == 80):
            points = points - 30
    else:
        print("You Lose")
        tries = tries + 1
        points = points - 20
    