import random

def funFactF():
  funFacts = open("facts.txt", "r")
  funFactL = []
  for line in funFacts:
    funFactL.append(line)
  
  funFact = random.choice(funFactL)
  print(funFact)