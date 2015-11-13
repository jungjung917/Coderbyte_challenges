"""
Using the Python language, have the function OffLineMinimum(strArr) take the strArr parameter being passed which will be an array of integers ranging from 1...n and the letter "E" and return the correct subset based on the following rules. The input will be in the following format: ["I","I","E","I",...,"E",...,"I"] where the I's stand for integers and the E means take out the smallest integer currently in the whole set. When finished, your program should return that new set with integers separated by commas. For example: if strArr is ["5","4","6","E","1","7","E","E","3","2"] then your program should return 4,1,5. 
"""

def OffLineMinimum(strArr):
    E_index = []
    list_out = []
    list_com = []
    for index,value in enumerate(strArr):
        if value == "E":
	    E_index.append(index)
    i = 0
    for index in E_index:
        list_com = list_com + strArr[i:index]
	list_out.append(min(list_com))
	list_com.remove(min(list_com))
	i = index+1
    return ','.join(str(num) for num in list_out)

print OffLineMinimum(["1","2","E","E","3"])
print OffLineMinimum(["4","E","1","E","2","E","3","E"])
