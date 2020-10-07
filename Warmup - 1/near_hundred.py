"""

Given an int n, return True if it is within 10 of 100 or 200. 

near_hundred(93) → True
near_hundred(90) → True
near_hundred(89) → False
"""

def near_hundred(n):
  plus = n + 10
  minus = n - 10
  if (plus >= 100 and plus < 111)  or (minus <= 100 and minus > 89) or (plus >= 200 and plus < 211) or (minus <= 200 and minus > 189):
    return True
  return False
    
