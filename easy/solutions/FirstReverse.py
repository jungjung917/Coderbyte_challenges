"""
 function FirstReverse(str) take the str parameter being passed and return the string in reversed order. 
"""
def FirstReverse(str): 
    str_out = ""
    for letter in str:
        str_out = letter + str_out
    return str_out
print FirstReverse("abcdefg")
