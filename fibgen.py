#Define tuple
def fib(a, b):
  return (b, a + b)

def fibgen(n=0):
  a = n
  b = n + 1
  while True:
    a, b = fib(a,b)
    yield b
