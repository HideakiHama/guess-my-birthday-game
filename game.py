from random import randint
#import randint from random library

guess_the_number = 1
#start number of time guessed by 1
month = randint(1, 12)
#month variable range from 1 to 12
year = randint(1924, 2004)
#year variable range from 1924 to 2004

your_name = input("Hi! What is your name? ")
# your_name = prompt the player for their name
print("Guess " + str(guess_the_number) + " : " + your_name + " were you born in " + str(month) + " / " + str(year) + " ?")
ask = input("yes or no?: ")
# print the following:
  # "Guess " + guess_the_number + " : " + your_name + " were you born in " + month + " / " + year + " ?"
  # ask = prompt the player with "yes or no?"
if ask == "yes":
  #if the user prompt yes the python saids "I knew it!" and exits the program
  print("I knew it!")
  exit()
else:
  # otherwise the pytho saids "Drat! Lemme try again"
  print("Drat! Lemme try again")


#The python guesses 5 more time

guess_the_number = 2

month = randint(1, 12)
year = randint(1924, 2004)
print("Guess " + str(guess_the_number) + " : " + your_name + " were you born in " + str(month) + " / " + str(year) + " ?")
ask = input("yes or no?: ")

if ask == "yes":
  print("I knew it!")
  exit()
else:
  print("Drat! Lemme try again")


guess_the_number = 3

month = randint(1, 12)
year = randint(1924, 2004)
print("Guess " + str(guess_the_number) + " : " + your_name + " were you born in " + str(month) + " / " + str(year) + " ?")
ask = input("yes or no?: ")

if ask == "yes":
  print("I knew it!")
  exit()
else:
  print("Drat! Lemme try again")


guess_the_number = 4

month = randint(1, 12)
year = randint(1924, 2004)
print("Guess " + str(guess_the_number) + " : " + your_name + " were you born in " + str(month) + " / " + str(year) + " ?")
ask = input("yes or no?: ")

if ask == "yes":
  print("I knew it!")
  exit()
else:
  print("Drat! Lemme try again")

guess_the_number = 5

month = randint(1, 12)
year = randint(1924, 2004)
print("Guess " + str(guess_the_number) + " : " + your_name + " were you born in " + str(month) + " / " + str(year) + " ?")
ask = input("yes or no?: ")

if ask == "yes":
  print("I knew it!")
  exit()
else:
  print("I have other things to do. Good bye.")
  exit()
  #Python exit the program
