"""
Using the Python language, have the function DivisionStringified(num1,num2) take both parameters being passed, divide num1 by num2, and return the result as a string with properly formatted commas. If an answer is only 3 digits long, return the number with no commas (ie. 2 / 3 should output "1"). For example: if num1 is 123456789 and num2 is 10000 the output should be "12,346". 
"""
def DivisionStringified(num1,num2):
    div_number = int(round(num1*1.0 / num2))  
    div_number_return = '{:,}'.format(div_number)
    return div_number_return
"""
    if div_number < 1000:
        div_number_return = str(div_number)
    else:
        while div_number >= 1000:
	    div_number_return =div_number_return +","+ str(div_number - (div_number//1000)*1000) 
	    div_number = div_number // 1000
	else:
	    div_number_return = str(div_number) + div_number_return
    return div_number_return
"""

print DivisionStringified(6874889900,67)
print DivisionStringified(5,2)
print DivisionStringified(1,10)
