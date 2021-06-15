import random

def hangman():
  print(" _,_  _, _, _  _, _, _  _, _, _")
  print("|_| /_\ |\ | / _ |\/| /_\ |\ |")
  print("| | | | | \| \ / |  | | | | \|")
  print("~ ~ ~ ~ ~  ~  ~  ~  ~ ~ ~ ~  ~")
  print()
  wordL = []
  wordF = open("words.txt", "r")
  for line in wordF:
    wordL.append(line)
  
  secretWord = random.choice(wordL)
  dashes = "-" * len(secretWord)
  guesses = 10

  def getGuess():
    while True:
      try:
        guess = str(input("Guess: "))
      except ValueError:
        print("Your guess must be a lowercase letter!")
      if len(guess) != 1:
        print("Your guess must have exactly one character!")
        continue
      elif guess.islower() != True:
        print("Your guess must be a lowercase letter!")
        continue
      elif type(guess) == str and len(guess) == 1 and guess.islower() == True:
        break
    return(guess)

  def updateDashes(secretWord, dashes, guesses):
    secretWordL = list(secretWord)
    dashes = list(dashes)
    while guesses > 0:
      print(str(guesses) + " Incorrect guesses left.")
      guess = getGuess()
      if guess in secretWordL:
        for i in range(len(secretWordL)):
          if guess == secretWordL[i]:
            dashes[i] = guess
      else:
        guesses -= 1
      print("".join(dashes))
      if "".join(dashes) == secretWord:
          print("You win!")
          break
    if guesses == 0:
      print("You lose!")
      print()
      print("The word was " + secretWord)
      print()
      print()

  updateDashes(secretWord, dashes, guesses)