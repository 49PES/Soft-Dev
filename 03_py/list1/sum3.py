# Given an array of ints length 3, return the sum of all the elements.

def sum3(nums):
  return sum(nums)

print( sum3([1, 2, 3]) ) # → 6	6	OK	
print( sum3([5, 11, 2]) ) # → 18	18	OK	
print( sum3([7, 0, 0]) ) # → 7	7	OK	
print( sum3([1, 2, 1]) ) # → 4	4	OK	
print( sum3([1, 1, 1]) ) # → 3	3	OK	
print( sum3([2, 7, 2]) ) # → 11	11	OK