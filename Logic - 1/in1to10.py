"""


Given a number n, return True if n is in the range 1..10,
inclusive. Unless outside_mode is True, in which case return
True if the number is less or equal to 1, or greater or equal to 10.


in1to10(5, False) → True
in1to10(11, False) → False
in1to10(11, True) → True

"""

def in1to10(n, outside_mode):
  if outside_mode and (n < 2 or n > 9):
    return True
  if outside_mode is False and n > 0  and n < 11:
    return True
  return False
