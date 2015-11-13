"""
Using the Python language, have the function ThirdGreatest(strArr) take the array of strings stored in strArr and return the third largest word within in. So for example: if strArr is ["hello", "world", "before", "all"] your output should be world because "before" is 6 letters long, and "hello" and "world" are both 5, but the output should be world because it appeared as the last 5 letter word in the array. If strArr was ["hello", "world", "after", "all"] the output should be after because the first three words are all 5 letters long, so return the last one. The array will have at least three strings and each string will only contain letters. 
"""
def ThirdGreatest(strArr):
    len_dic = {}
    for index, word in enumerate(strArr):
        len_dic[index] = len(word)
    for i in range(0,2):
        max_value = max(len_dic.values())
        for k,v in len_dic.items():
            if v == max_value:
	        del len_dic[k]
	        break
    keys = len_dic.keys()
    values = len_dic.values()
    max_index = values.index(max(len_dic.values()))

    return strArr[keys[max_index]]
print ThirdGreatest(["one","two","three"]) 
