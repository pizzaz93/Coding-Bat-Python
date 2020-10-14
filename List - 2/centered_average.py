"""

Return the "centered" average of an array of ints,
which we'll say is the mean average of the values, except ignoring
the largest and smallest values in the array. If there are multiple copies of
the smallest value, ignore just one copy, and likewise for the largest value.
Use int division to produce the final average. You may assume that the array is length 3 or more.


centered_average([1, 2, 3, 4, 100]) → 3
centered_average([1, 1, 5, 5, 10, 8, 7]) → 5
centered_average([-10, -4, -2, -4, -2, 0]) → -3

"""

def centered_average(nums):
  maxListNum = max(nums)
  minListNum = min(nums)
  numsTotal = 0
  listCount = 0
  maxListNumCounter = 0 
  minListNumCounter = 0
  for i in range(len(nums)):
    if nums[i] == maxListNum and maxListNumCounter == 0:
      maxListNumCounter += 1
      continue
    if nums[i] == minListNum and minListNumCounter == 0:
      minListNumCounter += 1
      continue
    numsTotal += nums[i]
    listCount += 1
  return numsTotal / listCount
