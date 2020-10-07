"""

Return True if the string "cat" and "dog" appear the same number of times in the given string.


cat_dog('catdog') → True
cat_dog('catcat') → False
cat_dog('1cat1cadodog') → True

"""

def cat_dog(str):
  catCounter = 0
  dogCounter = 0
  for x in range(len(str)):
    if str[x:x + 1] == "c" and str[x + 1:x + 2] == "a" and str[x + 2:x + 3] == "t":
      catCounter += 1
    if str[x:x + 1] == "d" and str[x + 1:x + 2] == "o" and str[x + 2:x + 3] == "g":
      dogCounter += 1  
  if catCounter == dogCounter:
    return True
  return False
