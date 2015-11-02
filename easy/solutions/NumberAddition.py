def NumberAddition(input_str):
    total = 0
    number = ""
    for letters in input_str:
        if letters.isdigit():
	    number = number + letters
	else:
	    number = number + " "
    
    numbers =  number.split(" ") 
    
    for num in numbers:
	if num.isdigit():
	    total += int(num)
    return total
					        
print NumberAddition("77Rando, 9")
print NumberAddition("5 hello 5")

