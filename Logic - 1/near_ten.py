"""

Given a non-negative number "num", return True if num is within 2 
of a multiple of 10. Note: (a % b) is the remainder of dividing a by b, 
so (7 % 5) is 2. See also: Introduction to Mod


near_ten(12) → True
near_ten(17) → False
near_ten(19) → True

"""

def near_ten(num):
  numOne = (num + 1) % 10
  numTwo = (num + 2) % 10
  numThree = (num - 1) % 10
  numFour = (num - 2) % 10
  if num % 10 == 0 or numOne == 0 or numTwo == 0 or numThree == 0 or numFour == 0:
    return True
  return False
  
