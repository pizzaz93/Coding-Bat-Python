"""

Return the number of times that the string "code" appears anywhere in the given string,
except we'll accept any letter for the 'd', so "cope" and "cooe" count.


count_code('aaacodebbb') → 1
count_code('codexxcode') → 2
count_code('cozexxcope') → 2

"""

def count_code(str):
  counter = 0
  for x in range(len(str)):
    if str[x:x + 1] == "c" and str[x + 1:x + 2] == "o" and str[x + 3:x + 4] == "e":
      counter += 1
  return counter
