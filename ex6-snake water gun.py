import random
lst = ["snake",  "water", "gun"]
choice = random.choice(lst)
print(" welcome t6o snake water gun game")
inpt = str(input("choose between snake, gun and water: "))
if inpt=="snake" and choice == "water":
    print("opponent is water \n snake drunk the water")
elif inpt == "snake" and choice == "gun":
    print("opponent is gun \nsnake died")
elif inpt == "water" and choice== "gun":
    print("opponent is gun\ngun damaged")
elif inpt == "water" and choice== "snake":
    print("opponent is snake \nwater is drunk")
elif inpt == "gun" and choice== "water":
    print("opponent is water \n your gun damaged")
elif inpt == "gun" and choice== "snake":
    print("opponent is snake \nyou killed the snake")
elif inpt == choice:
    print("both choose the same")