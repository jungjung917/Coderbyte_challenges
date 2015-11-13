"""
Using the Python language, have the function SecondGreatLow(arr) take the array of numbers stored in arr and return the second lowest and second greatest numbers, respectively, separated by a space. For example: if arr contains [7, 7, 12, 98, 106] the output should be 12 98. The array will not be empty and will contain at least 2 numbers. It can get tricky if there's just two numbers! 
"""
def SecondGreatLow(arr): 
    min_value = min(arr)
    max_value = max(arr)
    
    #for value in arr:
    #    if value == min_value:
    arr = [value for value in arr if value != min_value]
    arr = [value for value in arr if value != max_value]
    if len(arr) == 0:    
        return str(max_value)+ " " + str(min_value)
    else:
        return str(min(arr)) + " " + str(max(arr))
print SecondGreatLow([1,2,3,100])  
print SecondGreatLow([2,2,3,100])
