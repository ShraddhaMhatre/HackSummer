def fizzbuzz(n):
  # Integer --> String
  #if n % 3 == 0 and n % 5 == 0:
  if n % 15 == 0:
    return "FizzBuzz"
  elif n % 3 == 0:
    return "Fizz"
  elif n % 5 == 0:
    return "Buzz"
  else:
    return str(n)

def main():
  #DO FB for 30 steps
  STEPS = 30
  for i in range(1, STEPS+1):
    fb = fizzbuzz(i)
    print(fb)
  
main()
