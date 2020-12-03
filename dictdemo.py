import time

# then = time.time()
# now = time.time()
# print(now - then)

login_list = [
  ("Naruto", "Uzumaki"),
  ("Sasuke", "Uchiha"),
  ("Kakashi","Sensei"),
  ("Cardcaptor","Sakura")
]

login_dict = {
  "Naruto":"Uzumaki",
  "Sasuke":"Uchiha",
  "Kakashi":"Sensei",
  "Cardcaptor":"Sakura"
}

#input type(function itself, sequence, String)
def timetest(fn,seq,query):
  start = time.time()
  fn(seq, query)
  end = time.time()
  runtime = end - start
  return runtime


#input type(List, String)
def list_lookup(lst, query):
  for l in lst:
    if l[0] == query:
      return l[1]
  return None

def dict_lookup(dct, query):
  try:
    return dct[query]
  except KeyError:
    return None    
