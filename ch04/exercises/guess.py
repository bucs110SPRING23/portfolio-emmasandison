import random 

randnum = random.randrange(1,1001)
guess = int(input("Guess a number 1-1000: "))
count = 0
 

while guess != randnum:
    count += 1
    if guess < randnum:
        print("Too low")
        guess = int(input("Guess a number 1-1000: "))
    elif guess > randnum:
        print("Too high")
        guess = int(input("Guess a number 1-1000: "))
    elif randnum == guess: 
        print("Correct!", "The correct answer is randnum", "it took", count, "tries.")
        break 

