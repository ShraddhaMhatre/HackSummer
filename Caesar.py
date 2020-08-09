#Take the alphabet and a message
#Shift the letters message by x spaces
#Print the result

ALPHABET = "abcdefghijklmnopqrstuvwxyz"
SHIFT = 8
message = "hack summer!"

encrypted = ""

for c in message:
  if c in ALPHABET:
    idx = ALPHABET.find(c)
    new_idx = idx + SHIFT
    if new_idx < len(ALPHABET) - 1:
      encrypted += ALPHABET[new_idx]
    else:
      encrypted += ALPHABET[new_idx - len(ALPHABET)]
  else:
    encrypted += c
    
print(encrypted)