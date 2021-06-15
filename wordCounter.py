def wordCounter():
  print("__          __           _    _____                  _ ")
  print("\ \        / /          | |  / ____|                | |")
  print(" \ \  /\  / /__  _ __ __| | | |     ___  _   _ _ __ | |_ ___ _ __")
  print("  \ \/  \/ / _ \| '__/ _` | | |    / _ \| | | | '_ \| __/ _ \ '__|")
  print("   \  /\  / (_) | | | (_| | | |___| (_) | |_| | | | | ||  __/ |")
  print("    \/  \/ \___/|_|  \__,_|  \_____\___/ \__,_|_| |_|\__\___|_|")
  dictionary = {}

  sentence = input("String: ")
  sentence = sentence.split()

  for i in range(len(sentence)):
    if sentence[i] in dictionary:
      dictionary[sentence[i]] += 1
    else:
      dictionary[sentence[i]] = 1

  print(dictionary)
  print()