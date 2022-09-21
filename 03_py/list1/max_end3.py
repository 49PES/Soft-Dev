# Given an array of ints length 3, figure out which is larger, the first or last element in the array, and set all the other elements to be that value. Return the changed array.

def max_end3(nums):
  if nums[0] > nums[-1]:  
    return [nums[0]] * 3  # Cast the max value to a list, and then multiply the list by 3
  else: return [nums[-1]] * 3

print( max_end3([1, 2, 3]) ) # → [3, 3, 3]	[3, 3, 3]	OK	
print( max_end3([11, 5, 9]) ) # → [11, 11, 11]	[11, 11, 11]	OK	
print( max_end3([2, 11, 3]) ) # → [3, 3, 3]	[3, 3, 3]	OK	
print( max_end3([11, 3, 3]) ) # → [11, 11, 11]	[11, 11, 11]	OK	
print( max_end3([3, 11, 11]) ) # → [11, 11, 11]	[11, 11, 11]	OK	
print( max_end3([2, 2, 2]) ) # → [2, 2, 2]	[2, 2, 2]	OK	
print( max_end3([2, 11, 2]) ) # → [2, 2, 2]	[2, 2, 2]	OK	
print( max_end3([0, 0, 1]) ) # → [1, 1, 1]	[1, 1, 1]	OK
