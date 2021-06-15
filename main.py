import os
import ticTacToe as tTT
import hangman as hm
import wordCounter as wC
import phoneBook as pB
import owls as o
import wordLadder as wL
import removeFromString as rFS
import higherLower as hL
import rockPaperScissors as rPC
import facts as f


programs = ("Tic Tac Toe(2 player), Hangman, Word Counter, Phone book, Owls, Word Ladder, Remove From String, Higher Lower, Rock Paper Scissors, random fun fact, ")

def ifBored(programs):
  print()
  print(programs)
  print()
  while True:
    try:
      program = int(input("Which program would you like to run?(1st = 0, 2nd = 1, etc. -1 to exit, -2 to clear console): "))
      break
    except ValueError:
      print("Invalid input")
      continue
  print()
  if program == 0:
    tTT.ticTacToe()
  elif program == 1:
    hm.hangman()
  elif program == 2:
    wC.wordCounter()
  elif program == 3:
    pB.phoneBook()
  elif program == 4:
    o.owls()
  elif program == 5:
    wL.wordLadderProgram()
  elif program == 6:
    rFS.removeFromString()
  elif program == 7:
    hL.higherLower()
  elif program == 8:
    rPC.rockPaperScissors()
  elif program == 9:
    f.funFactF()   
  elif program == -1:
    exit
  elif program ==-2:
    os.system("clear")
  else:
    print("Invalid imput")
    print()

def checkBored(bored):
  if bored == "yes":
    return True
  elif bored == "no":
    print()
    print("nerd")
    print()
    print()
    return False

while True:
  while True:
    bored = input("Are you bored? (Yes/No): ").lower()
    if bored == "yes" or bored == "no":
      break
    else:
      print("Invalid")
      continue
  if checkBored(bored) == True:
    ifBored(programs)
  else:
    break
