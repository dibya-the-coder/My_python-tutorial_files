n = 10
guess = 1
print("you have 9 chances")
while (guess<=10):
    no = int(input("guess the no. "))
    if no < 10:
        print("you entered a smaller no.")
    elif no > 10:
        print("you entered a greater no.")
    else:
        print("yoo hoo..... you won\n")
        break
    print(9-guess,"no of guess left")
    guess = guess+1
if(guess>9):
    print("game over....")
