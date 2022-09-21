# Given an array of ints length 3, return an array with the elements "rotated left" so {1, 2, 3} yields {2, 3, 1}.

def rotate_left3(nums):
  return nums[1:] + [nums[0]] # This rotates everything from the 1st index to the last left, and adds the 0th element to the right

print( rotate_left3([1, 2, 3]) ) # → [2, 3, 1]	[2, 3, 1]	OK	
print( rotate_left3([5, 11, 9]) ) # → [11, 9, 5]	[11, 9, 5]	OK	
print( rotate_left3([7, 0, 0]) ) # → [0, 0, 7]	[0, 0, 7]	OK	
print( rotate_left3([1, 2, 1]) ) # → [2, 1, 1]	[2, 1, 1]	OK	
print( rotate_left3([0, 0, 1]) ) # → [0, 1, 0]	[0, 1, 0]	OK	