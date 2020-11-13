import random

def tree():
  #print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last = 13
  rnd = random.randint(0, last)
  
  end = 13
  pick = random.randint(0,end)
  
  print(quotes[rnd],' ',quotes[pick])
  #print(quotes[pick])

if __name__== "__main__":
  tree()
