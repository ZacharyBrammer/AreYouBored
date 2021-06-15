def owls():
  print("  ___")
  print(" (o,o)")
  print(" {`\"'}")
  print(" _\"_\"_          _")
  print("|  _  |        | |")
  print("| | | |_      _| |___")
  print("| | | \ \ /\ / / / __|")
  print("\ \_/ /\ V  V /| \__ \\")
  print(" \___/  \_/\_/ |_|___/")
  print()

  owls = input("Enter some text: ")

  count = owls.count("owl")

  owls = owls.split()

  owlIndexes = []

  for i in range(count):
      try:
          index = owls.index("owl")
      except ValueError:
          try:
              index = owls.index("owls")
          except ValueError:
              try:
                  index = owls.index("owls.")
              except ValueError:
                  try:
                      index = owls.index("owl's")
                  except ValueError:
                      try:
                          index = owls.index("owl.")
                      except ValueError:
                          print("Bruh wtf")
      if i >= 1:
          owlIndexes.append(index + 1)
      else:
          owlIndexes.append(index)
      owls = owls[:index] + owls[index + 1:]

  owlIndexes.sort()

  print("There were " + str(count) + " words that contained \"owl\".")

  print("They occurred at indices: " + str(owlIndexes))