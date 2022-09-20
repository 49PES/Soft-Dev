def string_times(str, n):
  return n * str

def front_times(str, n):
  if len(str) < 3:
    return str * n
  return str[:3] * n

def string_bits(str):
  s = ""
  for i in range(len(str)):
    if i % 2 == 0:
      s += str[i]
  return s

def string_splosion(str):
  s = ""
  for i in range(len(str) + 1):
    s += str[:i]
  return s

def last2(str):
  c = 0
  if (len(str) > 2):
    sub = str[len(str)-2:]
    str = str[:len(str)-1]
    for i in range(len(str)):
      if (str[i:i+2] == sub):
        c += 1
  return c

def array_count9(nums):
  c = 0
  for i in nums:
    if i == 9:
      c += 1
  return c

def array_front9(nums):
  if(len(nums) >= 4):
    return 9 in nums[:4] # (nums[0] == 9 or nums[1] == 9 or nums[2] == 9 or nums[3] == 9)
  return 9 in nums

def array123(nums):
  for i in range(len(nums)):
    if(nums[i] == 1):
      if(i + 2 >= len(nums)):
        return False
      if(nums[i + 1] == 2 and nums[i + 2] == 3):
        return True
        
  return False
  
def string_match(a, b):
  s = min(len(a), len(b))
  c = 0
  for i in range(s - 1):
    if (a[i:i+2] == b[i:i+2]):
      c += 1
  return c