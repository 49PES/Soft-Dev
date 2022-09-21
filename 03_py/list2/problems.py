# Return the number of even ints in the given array. Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.

def count_evens(nums):
  c = 0
  for i in nums:
    if i % 2 == 0:  # mod 2 = 0 indicates that a number has an even parity
      c += 1 
  return c

# Given an array length 1 or more of ints, return the difference between the largest and smallest values in the array. Note: the built-in min(v1, v2) and max(v1, v2) functions return the smaller or larger of two values.

def big_diff(nums):
  return max(nums) - min(nums)
  
# Return the "centered" average of an array of ints, which we'll say is the mean average of the values, except ignoring the largest and smallest values in the array. If there are multiple copies of the smallest value, ignore just one copy, and likewise for the largest value. Use int division to produce the final average. You may assume that the array is length 3 or more.

def centered_average(nums):
  # nums.sort()
  # sum = 0
  # for i in range(1, len(nums) - 1):
  #   sum += nums[i]
  # return sum // (len(nums) - 2)
  
  return ( sum(nums) - max(nums) - min(nums) ) // (len(nums) - 2) # The // is used as a Euclidean division to round down to an int

# Return the sum of the numbers in the array, returning 0 for an empty array. Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.

def sum13(nums):
  # sum = 0
  # for i in range(len(nums)):
  #   if(nums[i] != 13 or (i > 0 and nums[i - 1] != 13)):
  #     sum += nums[i]
  # return sum
  
  # sum = 0
  # for num in nums:
  #   if (num == 13):
  #     return sum
  
  sum = 0
  i = 0
  while (i < (len(nums)) ):
    if (nums[i] == 13):
      i = i + 1 # Skip 13, and add 1 to the index so that the next index will also be skipped after the second +1
    else:
      sum += nums[i]
    i += 1
  return sum

# Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 7 (every 6 will be followed by at least one 7). Return 0 for no numbers.

def sum67(nums):
  sum = 0
  on = True
  for i in range(len(nums)):
    if(nums[i] == 6):
      on = False
      
    if(on):
      sum += nums[i] 
      
    if(nums[i] == 7):
      on = True
      
  return sum
 
# Given an array of ints, return True if the array contains a 2 next to a 2 somewhere.

def has22(nums):
  for i in range(len(nums)):
    if(nums[i] == 2 and i + 1 < len(nums) and nums[i + 1] == 2):
      return True
  return False
