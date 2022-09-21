# Given an array of ints, return the sum of the first 2 elements in the array. If the array length is less than 2, just sum up the elements that exist, returning 0 if the array is length 0.

def sum2(nums):
  # sum = 0
  # if(len(nums) < 2):
  #   for i in nums:
  #     sum += i
  #   return sum
  # return nums[0] + nums[1]
  

  if len(nums) == 0:
    return 0
  elif (len(nums) < 2):
    return nums[0]
  return nums[0]+nums[1]

print( sum2([1, 2, 3]) ) # → 3	3	OK	
print( sum2([1, 1]) ) # → 2	2	OK	
print( sum2([1, 1, 1, 1]) ) # → 2	2	OK	
print( sum2([1, 2]) ) # → 3	3	OK	
print( sum2([1]) ) # → 1	1	OK	
print( sum2([]) ) # → 0	0	OK	
print( sum2([4, 5, 6]) ) # → 9	9	OK	
print( sum2([4]) ) # → 4	4	OK