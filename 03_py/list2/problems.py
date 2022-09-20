def count_evens(nums):
  c = 0
  for i in nums:
    if i % 2 == 0:
      c += 1
  return c

def big_diff(nums):
  return max(nums) - min(nums)
  

def centered_average(nums):
  # nums.sort()
  # sum = 0
  # for i in range(1, len(nums) - 1):
  #   sum += nums[i]
  # return sum // (len(nums) - 2)
  
  return ( sum(nums) - max(nums) - min(nums) ) // (len(nums) - 2)

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
      i = i + 1
    else:
      sum += nums[i]
    i += 1
  return sum

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
 
def has22(nums):
  for i in range(len(nums)):
    if(nums[i] == 2 and i + 1 < len(nums) and nums[i + 1] == 2):
      return True
  return False
