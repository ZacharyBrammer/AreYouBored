def removeFromString():
  def remove_all_from_string(x, y):
      if len(y) >= 0:
          while y in x:
              yLocation = x.find(y)
              x = x[:yLocation] + "" + x[yLocation + 2:]
          else:
              return x
  
  print("In this program, you will type a string and select a part of it to remove. Ex: Bananas, an would give you bas")
  print()
  x = input("String: ")
  print()
  y = input("Part to remove: ")

  print(remove_all_from_string(x, y))