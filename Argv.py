import sys

#Starts with arg[0] and prints main.py (file name)
#for a in sys.argv:

#Starts with arg[0]
#for a in sys.argv[1:]:
#  print(a)
#print("Hello, Bash!")

for a in sys.argv[1:]:
  greeting = "Hello, {}!".format(a)
  print(greeting)