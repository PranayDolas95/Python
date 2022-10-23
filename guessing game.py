import random

i = random.randint(0, 12)
t = 0
print ("i")

while(t == 0):
    j = int(input("Guess the number :- "))

    if(j == i):
        print("you won")
        break

    else:
        print("you lose")    
        t = t + 1
