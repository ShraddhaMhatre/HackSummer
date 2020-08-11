text = open("moby.txt")

lines = text.readlines()
#print(lines[0])

# (CHAP, WORD), (CHAP, WORD)

chapters = [[]]

current_chapter = 0

for i in range(len(lines)):
  line = lines[i].strip()
  words = line.split(" ")
  if "CHAPTER" in words:
    current_chapter += 1
    chapters.append(words)
  else:
    chapters[current_chapter] += words
