"""
Given a non-empty string like "Code" return a string like "CCoCodCode".


string_splosion('Code') → 'CCoCodCode'
string_splosion('abc') → 'aababc'
string_splosion('ab') → 'aab'
"""
def string_splosion(str):
  newStr = ""
  indexed = len(str)
  for x in range(indexed):
    if x == 0:
      newStr += str[x: x + 1]
    else:  
      newStr += str[0:x + 1]
  return newStr   
