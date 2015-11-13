"""
Using the Python language, have the function MeanMode(arr) take the array of numbers stored in arr and return 1 if the mode equals the mean, 0 if they don't equal each other (ie. [5, 3, 3, 3, 1] should return 1 because the mode (3) equals the mean (3)). The array will not be empty, will only contain positive integers, and will not contain more than one mode. 
"""

def MeanMode(arr): 
    count_dic = {}
    mean = int(sum(arr) *1.0 / len(arr))
    for i in arr:
        count_dic[i] = arr.count(i)
    mode_count = max(count_dic.values())
    for k,v in count_dic.items():
	if v == mode_count:
	    mode = k
    if mean == mode :
        return 1
    else: 
        return 0
print MeanMode([4, 4, 4, 6, 2])
print MeanMode([1,2,3])
