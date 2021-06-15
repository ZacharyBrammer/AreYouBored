import random

def rockPaperScissors():
  choices = ["r", "p", "s"]
  while True:
    usrChoice = input("Rock, Paper or Scissors? (R, P, S): ").lower()
    if usrChoice.lower() == "r" or usrChoice.lower() == "p" or usrChoice.lower() == "s":
      break
    else:
      print("Invalid input")
      continue
  
  compChoice = random.choice(choices)
  usrChoiceText = ("You chose: ")
  compChoiceText = ("The computer chose: ")
  usrWins = ("You Won!")
  compWins = ("You Lost :(")

  if usrChoice == "r" and compChoice == "s":
    print(usrChoiceText + "rock")
    print(compChoiceText + "scissors")
    print(usrWins)
  elif usrChoice == "s" and compChoice == "p":
    print(usrChoiceText + "scissors")
    print(compChoiceText + "paper")
    print(usrWins)
  elif usrChoice == "p" and compChoice == "r":
    print(usrChoiceText + "paper")
    print(compChoiceText + "rock")
    print(usrWins)
  elif usrChoice == "s" and compChoice == "r":
    print(usrChoiceText + "scissors")
    print(compChoiceText + "rock")
    print(compWins)
  elif usrChoice == "p" and compChoice == "s":
    print(usrChoiceText + "paper")
    print(compChoiceText + "scissors")
    print(compWins)
  elif usrChoice == "r" and compChoice == "p":
    print(usrChoiceText + "rock")
    print(compChoiceText + "paper")
    print(compWins)
  elif usrChoice == "r" and compChoice == "r":
    print(usrChoiceText + "rock")
    print(compChoiceText + "rock")
    print("It's a Tie!")
  elif usrChoice == "p" and compChoice == "p":
    print(usrChoiceText + "paper")
    print(compChoiceText + "paper")
    print("It's a Tie!")
  elif usrChoice == "s" and compChoice == "s":
    print(usrChoiceText + "scissors")
    print(compChoiceText + "scissors")
    print("It's a Tie!")
  print()
  print()