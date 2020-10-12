"""

Given an array of ints length 3, return a new array with
the elements in reverse order, so {1, 2, 3} becomes {3, 2, 1}.


reverse3([1, 2, 3]) → [3, 2, 1]
reverse3([5, 11, 9]) → [9, 11, 5]
reverse3([7, 0, 0]) → [0, 0, 7]

"""

def reverse3(nums):
  newList = nums
  x = newList.pop(0)
  y = newList.pop(0)
  newList.append(y)
  newList.append(x)
  return newList
