def tree():
  #print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  print(quotes[1])

if __name__== "__tree__":
  tree()
