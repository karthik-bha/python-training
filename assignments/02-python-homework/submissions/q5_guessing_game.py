import random
a = random.randrange(1,101)
count = 0   
while True:
    b = int(input("Guess the number: "))
    count+=1
    if a == b:
        print(f"Correct! You guessed it in {count} attempts")
        break
    elif b < a:
        print("Too low!")
    else:
        print("Too high!")