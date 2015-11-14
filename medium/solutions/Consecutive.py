"""
Using the Python language, have the function Consecutive(arr) take the array of integers stored in arr and return the minimum number of integers needed to make the contents of arr consecutive from the lowest number to the highest number. For example: If arr contains [4, 8, 6] then the output should be 2 because two numbers need to be added to the array (5 and 7) to make it a consecutive array of numbers from 4 to 8. Negative numbers may be entered as parameters and no array will have less than 2 elements. 
"""
def Consecutive(arr):
    list_arr = sorted(arr)
    sum_number = 0
    for i in range(0,len(list_arr)-1):
        if list_arr[i+1] - list_arr[i]-1 == 0:
	    sum_number = sum_number
	else:
	    sum_number = sum_number + (list_arr[i+1] - list_arr[i] - 1)
    return sum_number
print Consecutive([5,10,15])
print Consecutive([5,12,15,17,18,22])
