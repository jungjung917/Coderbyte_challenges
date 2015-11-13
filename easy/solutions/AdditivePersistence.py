"""
Using the Python language, have the function AdditivePersistence(num) take the num parameter being passed which will always be a positive integer and return its additive persistence which is the number of times you must add the digits in num until you reach a single digit. For example: if num is 2718 then your program should return 2 because 2 + 7 + 1 + 8 = 18 and 1 + 8 = 9 and you stop at 9. 
"""
def AdditivePersistence(num):
    if num < 10:
        return 0
    else: 
        num_list = []
        for digit in str(num):
	    num_list.append(digit)
	sum_num = 0
	for number in num_list:
	    sum_num += int(number)
	if sum_num < 10:
	    return 1
	else:
	    return 1 + AdditivePersistence(sum_num)

print AdditivePersistence(4)
print AdditivePersistence(19)
