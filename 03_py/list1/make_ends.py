# Given an array of ints, return a new array length 2 containing the first and last elements from the original array. The original array will be length 1 or more.

def make_ends(nums):
  return [nums[0]] + [nums[-1]] # Cast both first and last elements to a list so you can concatenate them together

print( make_ends([1, 2, 3]) ) # → [1, 3]	[1, 3]	OK	
print( make_ends([1, 2, 3, 4]) ) # → [1, 4]	[1, 4]	OK	
print( make_ends([7, 4, 6, 2]) ) # → [7, 2]	[7, 2]	OK	
print( make_ends([1, 2, 2, 2, 2, 2, 2, 3]) ) # → [1, 3]	[1, 3]	OK	
print( make_ends([7, 4]) ) # → [7, 4]	[7, 4]	OK	
print( make_ends([7]) ) # → [7, 7]	[7, 7]	OK	
print( make_ends([5, 2, 9]) ) # → [5, 9]	[5, 9]	OK	
print( make_ends([2, 3, 4, 1]) ) # → [2, 1]	[2, 1]	OK