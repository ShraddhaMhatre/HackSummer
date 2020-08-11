from bookcipher import *

cipher = []

message = "I love whales".split(" ")

for m in message:
  print(m)
  found_m = False
  for i in range(len(chapters)):
    #words of i'th chapter
    words = chapters[i]
    for o in range(len(words)):
      word = words[o]
      if word == m:
        found_m = True
        cipher.append((i,o))
        break
    if found_m:
      break
  if found_m:
    found_m = False
    continue
  else:
    print(" Can't make message with this book!")
    break   

print(cipher)     


