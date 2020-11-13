import random

def tree():
  #print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last = 13
  rnd = random.sample(range(last),2)
  
  a = rnd[0]
  b = rnd[1]
  
  print(quotes[a],quotes[b], sep='')
  #print(quotes[pick])

if __name__== "__main__":
  tree()
