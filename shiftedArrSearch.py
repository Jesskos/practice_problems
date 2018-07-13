def linear_search(shiftArr, num):
  for index in range(len(shiftArr)):
    if shiftArr[index] == num:
      return index
  return -1

def binary_search(shiftArr, num):
  count = 0 
  midpoint = len(shiftArr)/2
  while count <= len(shiftArr):
    if shiftArr[midpoint] == num:
      return midpoint 
    elif shiftArr[midpoint] > num: 
      midpoint = midpoint - 1 
    elif shiftArr[midpoint] < num:
      midpoint = midpoint + 1 
  return -1 
  
def shifted_arr_search(shiftArr, num):
  mode = 1
  if mode == 1:
    return linear_search(shiftArr, num)
  else:
    return binary_search(shiftArr, num)