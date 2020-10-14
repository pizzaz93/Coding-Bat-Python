"""

Given an array of ints, return True
if the array contains a 2 next to a 2 somewhere.


has22([1, 2, 2]) → True
has22([1, 2, 1, 2]) → False
has22([2, 1, 2]) → False

"""

def has22(nums):
  counter = 0
  for i in range(len(nums)):
    if nums[i] == 2:
      counter += 1
    if counter > 1:
      return True
    if nums[i] != 2 and counter > 0:
      counter -= 1
  return False
