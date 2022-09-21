# Given an int array length 2, return True if it contains a 2 or a 3.

def has23(nums):
  return 2 in nums or 3 in nums

print( has23([2, 5]) ) # → True	True	OK	
print( has23([4, 3]) ) # → True	True	OK	
print( has23([4, 5]) ) # → False	False	OK	
print( has23([2, 2]) ) # → True	True	OK	
print( has23([3, 2]) ) # → True	True	OK	
print( has23([3, 3]) ) # → True	True	OK	
print( has23([7, 7]) ) # → False	False	OK	
print( has23([3, 9]) ) # → True	True	OK	
print( has23([9, 5]) ) # → False	False	OK