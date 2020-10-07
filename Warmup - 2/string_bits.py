"""
Given a string, return a new string made of every other char
starting with the first, so "Hello" yields "Hlo".


string_bits('Hello') → 'Hlo'
string_bits('Hi') → 'H'
string_bits('Heeololeo') → 'Hello'
"""

def string_bits(str):
  newStr = ""
  indexed = len(str)
  if indexed > 2:
    newStr += str[0:1]
    for x in range(indexed):
      if x % 2 == 0 and x != 0:
        newStr += str[x]
    return newStr      
  return str[0:1]
