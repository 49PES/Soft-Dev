# Given an array of ints, return True if 6 appears as either the first or last element in the array. The array will be length 1 or more.

def first_last6(nums):
  return nums[0] == 6 or nums[len(nums)-1] == 6


print( first_last6([1, 2, 6]) ) # → True	True	OK	
print( first_last6([6, 1, 2, 3]) ) # → True	True	OK	
print( first_last6([13, 6, 1, 2, 3]) ) # → False	False	OK	
print( first_last6([13, 6, 1, 2, 6]) ) # → True	True	OK	
print( first_last6([3, 2, 1]) ) # → False	False	OK	
print( first_last6([3, 6, 1]) ) # → False	False	OK	
print( first_last6([3, 6]) ) # → True	True	OK	
print( first_last6([6]) ) # → True	True	OK	
print( first_last6([3]) ) # → False	False	OK	
print( first_last6([5, 6]) ) # → True	True	OK	
print( first_last6([5, 5]) ) # → False	False	OK	
print( first_last6([1, 2, 3, 4, 6]) ) # → True	True	OK	
print( first_last6([1, 2, 3, 4]) ) # → False	False	OK	

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

# Return an int array length 3 containing the first 3 digits of pi, {3, 1, 4}.

def make_pi():
  return [3, 1, 4]
 
make_pi() ) # → [3, 1, 4]

# Given 2 arrays of ints, a and b, return True if they have the same first element or they have the same last element. Both arrays will be length 1 or more.

def common_end(a, b):
  return a[0] == b[0] or a[len(a)-1] == b[len(b)-1]

print( common_end([1, 2, 3], [7, 3]) ) # → True	True	OK	
print( common_end([1, 2, 3], [7, 3, 2]) ) # → False	False	OK	
print( common_end([1, 2, 3], [1, 3]) ) # → True	True	OK	
print( common_end([1, 2, 3], [1]) ) # → True	True	OK	
print( common_end([1, 2, 3], [2]) ) # → False	False	OK	

# Given an array of ints length 3, return the sum of all the elements.

def sum3(nums):
  return sum(nums)

print( sum3([1, 2, 3]) ) # → 6	6	OK	
print( sum3([5, 11, 2]) ) # → 18	18	OK	
print( sum3([7, 0, 0]) ) # → 7	7	OK	
print( sum3([1, 2, 1]) ) # → 4	4	OK	
print( sum3([1, 1, 1]) ) # → 3	3	OK	
print( sum3([2, 7, 2]) ) # → 11	11	OK

# Given an array of ints length 3, return an array with the elements "rotated left" so {1, 2, 3} yields {2, 3, 1}.

def rotate_left3(nums):
  return nums[1:] + [nums[0]] # This rotates everything from the 1st index to the last left, and adds the 0th element to the right

print( rotate_left3([1, 2, 3]) ) # → [2, 3, 1]	[2, 3, 1]	OK	
print( rotate_left3([5, 11, 9]) ) # → [11, 9, 5]	[11, 9, 5]	OK	
print( rotate_left3([7, 0, 0]) ) # → [0, 0, 7]	[0, 0, 7]	OK	
print( rotate_left3([1, 2, 1]) ) # → [2, 1, 1]	[2, 1, 1]	OK	
print( rotate_left3([0, 0, 1]) ) # → [0, 1, 0]	[0, 1, 0]	OK	

# Given an array of ints length 3, return a new array with the elements in reverse order, so {1, 2, 3} becomes {3, 2, 1}.

def reverse3(nums):
  return nums[::-1] # -1 here is a negative iterator: so this returns the list in reverse order

print( reverse3([1, 2, 3]) ) # → [3, 2, 1]	[3, 2, 1]	OK	
print( reverse3([5, 11, 9]) ) # → [9, 11, 5]	[9, 11, 5]	OK	
print( reverse3([7, 0, 0]) ) # → [0, 0, 7]	[0, 0, 7]	OK	
print( reverse3([2, 1, 2]) ) # → [2, 1, 2]	[2, 1, 2]	OK	
print( reverse3([1, 2, 1]) ) # → [1, 2, 1]	[1, 2, 1]	OK	
print( reverse3([2, 11, 3]) ) # → [3, 11, 2]	[3, 11, 2]	OK	
print( reverse3([0, 6, 5]) ) # → [5, 6, 0]	[5, 6, 0]	OK	
print( reverse3([7, 2, 3]) ) # → [3, 2, 7]	[3, 2, 7]	OK

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

# Given 2 int arrays, a and b, each length 3, return a new array length 2 containing their middle elements.

def middle_way(a, b):
  return [a[1]] + [b[1]]

print( middle_way([1, 2, 3], [4, 5, 6]) ) # → [2, 5]	[2, 5]	OK	
print( middle_way([7, 7, 7], [3, 8, 0]) ) # → [7, 8]	[7, 8]	OK	
print( middle_way([5, 2, 9], [1, 4, 5]) ) # → [2, 4]	[2, 4]	OK	
print( middle_way([1, 9, 7], [4, 8, 8]) ) # → [9, 8]	[9, 8]	OK	
print( middle_way([1, 2, 3], [3, 1, 4]) ) # → [2, 1]	[2, 1]	OK	
print( middle_way([1, 2, 3], [4, 1, 1]) ) # → [2, 1]	[2, 1]	OK

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