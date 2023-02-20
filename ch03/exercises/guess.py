import random 

randnum = random.randint(1,11)
guess = int(input("Guess a number 1-10: "))
attempts = 3

for attempt in range(attempts): 
  if randnum == guess: 
    print("Correct!")
    break
  else:
    if guess < randnum:
       print("Too low")
    if guess > randnum: 
       print("Too high")

    