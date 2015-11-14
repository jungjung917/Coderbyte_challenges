"""
Using the Python language, have the function SimpleMode(arr) take the array of numbers stored in arr and return the number that appears most frequently (the mode). For example: if arr contains [10, 4, 5, 2, 4] the output should be 4. If there is more than one mode return the one that appeared in the array first (ie. [5, 10, 10, 6, 5] should return 5 because it appeared first). If there is no mode return -1. The array will not be empty. 
"""
def SimpleMode(arr):
    table = {}
    for num in arr:
        if num in table:
	    table[num] = table.get(num) + 1
	else:
	    table[num] = 1
    if max(table.values()) == 1:
        return -1
    else:
        mode_keys = [k for k,v in table.items() if v == max(table.values())]
        for num in arr:
	    if num in mode_keys:
	        return num
		break
print SimpleMode([5,5,2,2,1])
