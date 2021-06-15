import random

def higherLower():
  def guessNumber():
      my_float = random.uniform(1.000, 999.999)
      while True:
          guess = float(input("Guess a number: "))
          if (round(guess, 2) == round(my_float, 2)):
              print("Correct!")
              print()
              break
          if (round(guess, 2) < round(my_float, 2)):
              print("Too low!")
              continue
          if (round(guess, 2) > round(my_float, 2)):
              print("Too high!")
              continue

  guessNumber()