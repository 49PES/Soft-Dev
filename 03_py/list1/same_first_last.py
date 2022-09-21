# Given an array of ints, return True if the array is length 1 or more, and the first element and the last element are equal.

def same_first_last(nums):
  return len(nums) >= 1 and nums[0] == nums[len(nums)-1] 

print( same_first_last([1, 2, 3]) ) # → False	False	OK	
print( same_first_last([1, 2, 3, 1]) ) # → True	True	OK	
print( same_first_last([1, 2, 1]) ) # → True	True	OK	
print( same_first_last([7]) ) # → True	True	OK	
print( same_first_last([]) ) # → False	False	OK	
print( same_first_last([1, 2, 3, 4, 5, 1]) ) # → True	True	OK	
print( same_first_last([1, 2, 3, 4, 5, 13]) ) # → False	False	OK	
print( same_first_last([13, 2, 3, 4, 5, 13]) ) # → True	True	OK	
print( same_first_last([7, 7]) ) # → True	True	OK