import random 

randnum = random.randrange(1,11)
attempts = 0

for _ in range(3): 
    guess = int(input("Guess a number 1-10: "))
    attempts = attempts + 1
    if guess < randnum:
        print("Too low")
    elif guess > randnum:
        print("Too high")
    elif randnum == guess: 
        print("Correct!")
        break

print("It took", attempts, "guesses")




