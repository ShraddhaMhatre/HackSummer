ALPHABET = "abcdefghijklmnopqrstuvwxyz"

def substitute(letter,shift):
  if letter in ALPHABET:
    idx = ALPHABET.find(letter)+shift
    return ALPHABET[idx%len(ALPHABET)]

  return letter

def caesar(msg,shift):
  encrypted = ""
  for c in msg:
    encrypted += substitute(c,shift)
  return encrypted

