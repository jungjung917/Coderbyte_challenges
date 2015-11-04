"""Take a str parameter being passed and return a compressed version of the string using the Run-length encoding algorithm. This algorithm works by taking the occurrence of each repeating character and outputting that number along with a single character of the repeating sequence. For example: "wwwggopp" would return 3w2g1o2p. The string will not contain any numbers, punctuation, or symbols.
"""
def RunLength(input_str):
    out_str = ""
    count = 1
    letter = input_str[0]

    for i  in range(1,len(input_str)):
	if letter == input_str[i]:
            count += 1
            letter = input_str[i]
	    if i == len(input_str) - 1 :
	        out_str = out_str + str(count) + letter
	else:
	    out_str = out_str + str(count) + letter
	    letter = input_str[i]
	    count = 1
	    if i == len(input_str) - 1 :
	        out_str = out_str + str(count) + letter
    return out_str
         
print RunLength("wwwggopp")
print RunLength("aabbccd")        
