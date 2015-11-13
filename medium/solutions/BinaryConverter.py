"""
Using the Python language, have the function BinaryConverter(str) return the decimal form of the binary value. For example: if 101 is passed return 5, or if 1000 is passed return 8. 
"""
def BinaryConverter(str):
    number_list = []
    binary_value = 0
    for num in str:
        number_list.append(int(num))
   
    for i in range(0,len(number_list)):
        if number_list[i] == 1:
	    binary_value = binary_value + 2 ** (len(number_list) -1-i) 
    return binary_value
print BinaryConverter("100101")
