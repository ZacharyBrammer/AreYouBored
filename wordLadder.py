def wordLadderProgram():
  print("╠═══╣")
  print("╠═══╣")
  print("╠═══╣")
  print("╠═══╣")
  print("╠═══╣")
  print("  _   _   _   _     _   _   _   _   _   _")
  print(" / \ / \ / \ / \   / \ / \ / \ / \ / \ / \\")
  print("( w | o | r | d ) ( l | a | d | d | e | r )")
  print(" \_/ \_/ \_/ \_/   \_/ \_/ \_/ \_/ \_/ \_/")
  print("")
  
  startWord = input("Give a starting word: ")
  startWordLen = len(startWord) - 1

  def getIndex():
    print()
    print("Remember, 0 is first letter, 1 is second, 2 is third, etc")
    while 1 > 0:
      try:
        index = int(input("Enter an index (-1 to quit): "))
      except ValueError:
        index = 999999999
      if index <= startWordLen and index >= 0 or index == -1:
        return index
        break
      else:
        print("Invalid index")
        continue
      
      
  def getLetter():
    while 1 > 0:
      letter = input("Enter a letter: ")
      if len(letter) > 1:
        print("Must be exactly one character!")
        continue
      else:
        rightLen = True
      isLetterLower = letter.islower()
      if isLetterLower == False:
        print("Character must be a lowercase letter!")
        continue
      if rightLen == True and isLetterLower == True:
        return letter
        break
      else:
        continue

  def wordLadder():
    index = getIndex()
    letter = getLetter()
    word = list(startWord)
    word[index] = letter
    word = "".join(word)
    print()
    print(word)
    while 1 > 0:
      index = getIndex()
      if index == -1:
        break
      letter = getLetter()
      word = list(word)
      word[index] = letter
      word = "".join(word)
      print(word)

  wordLadder()