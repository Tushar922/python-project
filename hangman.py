import random

words = ["apple", "banana", "cherry", "dragonfruit", "elderberry", "fig"]

word = random.choice(words)

guessed_letters = []

incorrect_guesses = 0

def display_game_state():
  print("Word: ", end="")
  for letter in word:
    if letter in guessed_letters:
      print(letter, end="")
    else:
      print("_", end="")
  print("\n")

  print("   +---+")
  print("       |")
  print("       |")
  print("       |")
  print("       |")
  print(" =========")

  if incorrect_guesses >= 1:
    print("   O")
  if incorrect_guesses >= 2:
    print("   |")
  if incorrect_guesses >= 3:
    print("  /|\\")
  if incorrect_guesses >= 4:
    print("  /")
  if incorrect_guesses >= 5:
    print("  / \ ")

while True:
  display_game_state()

  guess = input("Guess a letter: ").lower()

  if guess in guessed_letters:
    print("You already guessed that letter. Try again.")
  else:
    guessed_letters.append(guess)

    if guess in word:
      print("Correct guess!")
    else:
      print("Incorrect guess.")
      incorrect_guesses += 1

    if all(letter in guessed_letters for letter in word):
      print("Congratulations! You guessed the word!")
      break
    elif incorrect_guesses >= 6:
      print("You ran out of guesses. The word was:", word)
      break