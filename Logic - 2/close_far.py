"""

Given three ints, a b c, return True if two of a, b or c is "close" 
(is equal or differing from another value by 1), while the other is "far",
(differing from both other values by 2 or more).


close_far(1, 2, 10) → True
close_far(1, 2, 3) → False
close_far(4, 1, 3) → True

"""

def close_far(a, b, c):
  d = abs(a)
  e = abs(b)
  f = abs(c)
  if (e == f or e + 1 == f or e - 1 == f) and  (e - 1 != d and e + 1 != d) and (f - 1 != d and f + 1 != d) :
    return True
  if (d == e or d + 1 == e or d - 1 == e) and  (d - 1 != f and d + 1 != f) and (e - 1 != f and e + 1 != f):
    return True
  if (d == f or d + 1 == f or d - 1 == f) and  (d - 1 != e and d + 1 != e) and (f - 1 != e and f + 1 != e):
    return True
  return False
