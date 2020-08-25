import random
from fibgen import *

ALPHABET = "abcdefghijklmnopqrstuvwxyz"

def pad(padd_length):
  padding = ""
  while len(padding) <= padd_length:
    padding += random.choice(ALPHABET)
  return padding

def obscure(msg):
  encrypted = ""
  gen = fibgen(1)

  for c in msg:
    fib_num = next(gen)
    encrypted += c
    encrypted += pad(fib_num)

  return encrypted

def main():
  msg = "Hello!"
  print(obscure(msg))

main()
