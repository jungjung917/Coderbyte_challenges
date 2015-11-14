"""
the function ArrayAddition(arr) take the array of numbers stored in arr and return the 
string true if any combination of numbers in the array can be added up to equal the 
largest number in the array, otherwise return the string false. For example: 
if arr contains [4, 6, 23, 10, 1, 3] the output should return true 
because 4 + 6 + 10 + 3 = 23. The array will not be empty, 
will not contain all the same elements, and may contain negative numbers. 
"""

def ArrayAddition(arr): 

  max_value = max(arr)
  arr.pop(arr.index(max(arr)))
  print max_value, arr
  def findconbination(arr):
      if len(arr):
          return "false"
      else:
          sum = 0
          i = 0
          while i < len(arr):
              sum = sum + arr[i]
              print sum
              if sum == max_value:
                  return "true"
              else: 
                  i = i + 1
          
          findconbination(arr.pop(0))
  return findconbination(arr)
print ArrayAddition([1,2,3,100]) 
print ArrayAddition([3,5,-1,8,12])

