#This is guess the random number game
import random

print("Hello. What is your name?")
name = input()

print("Well, " + name + ", I am thinking of number between 1 and 20")
secretNumber = random.randint(1, 20)

for guessesTaken in range(1,7):
  print("Take a guess.")
  guess = int(input())

  if guess < secretNumber:
    print("Your guess is too low!")
  elif guess > secretNumber:
    print("Your guess is too high!")
  else:
    break #This is for correct guess
  
if guess == secretNumber:
  print("That's great, " + name +"! You have guessed it in " + str(guessesTaken) + "guesses.")
else:
  print("Nope! The number I was thinking of was " + str(secretNumber))