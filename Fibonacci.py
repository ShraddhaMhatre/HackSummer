#Defining a tuple
def fib(a, b):
  return (b, a+b)

def fibonacci(steps):
  a = 0
  b = 1
  for i in range(steps):
    a, b = fib(a, b)
    print(b)

def main():
  STEPS = input("Enter number of steps")
  fibonacci(int(STEPS))

main()