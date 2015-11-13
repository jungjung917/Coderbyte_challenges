"""
Using the Python language, have the function DashInsert(str) insert dashes ('-') between each two odd numbers in str. For example: if str is 454793 the output should be 4547-9-3. Don't count zero as an odd number. 
"""
def DashInsert(str):
    count = 0
    str_out = ""
    for num in str:
        if int(num) % 2 == 0:
	    count = 0
	else:
	    count = count + 1
	
	if count >= 2:
	    str_out = str_out + "-" + num
	else: 
	    str_out = str_out + num
    return str_out
print DashInsert("99946")
