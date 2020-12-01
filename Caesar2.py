import sys
#python caesar2.py "hello" 3 > output.txt
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

def main():
  clear_text = sys.argv[1]
  shift = int(sys.argv[2])
  print(caesar(clear_text,shift))

main()
