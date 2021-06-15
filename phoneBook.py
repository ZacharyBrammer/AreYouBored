def phoneBook():
  print(" , __  _                         , __            _ ")
  print("/|/  \| |                       /|/  \          | |")
  print(" |___/| |     __   _  _    _     | __/ __   __  | |")
  print(" |    |/ \   /  \_/ |/ |  |/     |   \/  \_/  \_|/_)")
  print(" |    |   |_/\__/   |  |_/|__/   |(__/\__/ \__/ | \_/")
  print()

  phoneBook = {}

  while True:
    name = input("Name: ")
    if name in phoneBook:
      print("Phone number: " + phoneBook[name])
    elif name == "":
      break
    else:
      number = input("Not in phonebook. What is their number: ")
      phoneBook[name] = number

  print(phoneBook)