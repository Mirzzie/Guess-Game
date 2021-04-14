# Game description

print("##### Welcome to guess game ##### \n")
print("""########### Info ###########)
Guess a one digit number
You have only 3 chances to win\n""")

#Game code

guess_limit = 3
secret_number = 5
guess_count = 0
while guess_count < guess_limit:
  guess = int(input("Enter the guessed number:"))
  if guess != secret_number:
      if guess_count == 2:
          print("You lose! :/")
          break
      print("Sorry! Try Again :/")
      guess_count = guess_count + 1
  else:
      print("You Won! :)")
      break

