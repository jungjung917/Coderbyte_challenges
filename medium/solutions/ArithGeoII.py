"""
the function ArithGeoII(arr) take the array of numbers stored in arr and return the string "Arithmetic" if the sequence follows an arithmetic pattern or return "Geometric" if it follows a geometric pattern. If the sequence doesn't follow either pattern return -1. An arithmetic sequence is one where the difference between each of the numbers is consistent, where as in a geometric sequence, each term after the first is multiplied by some constant or common ratio. Arithmetic example: [2, 4, 6, 8] and Geometric example: [2, 6, 18, 54]. Negative numbers may be entered as parameters, 0 will not be entered, and no array will contain all the same elements. 
"""
def ArithGeoII(arr):
    diff = arr[1] - arr[0]
    ratio = arr[1] /  arr[0]
    i = 2
    result1 = list()
    result2 = list()
    while i < len(arr):
    	if arr[i] != diff + arr[i-1]:
	    if arr[i] != ratio * arr[i-1]:
	        return -1
	    else:
	        i = i + 1
                result1.append(True)
	else:
	    i = i + 1
	    result1.append(False)

    if all(result1):
        return "Geometric"
    else:
        return "Arithmetic"
	    
print ArithGeoII([1,2,3,100])
print ArithGeoII([5,10,15])
print ArithGeoII([2,4,16,24])
