"""
Return the number of times that the string "hi" appears anywhere in the given string.


count_hi('abc hi ho') → 1
count_hi('ABChi hi') → 2
count_hi('hihi') → 2

"""

def count_hi(str):
  counter = 0
  for x in range(len(str)):
    if str[x:x + 1] == "h" and str[x + 1:x + 2] == "i":
      counter += 1
  return counter
