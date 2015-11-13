"""
Using the Python language, have the function LetterCount(str) take the str parameter being passed and return the first word with the greatest number of repeated letters. For example: "Today, is the greatest day ever!" should return greatest because it has 2 e's (and 2 t's) and it comes before ever which also has 2 e's. If there are no words with repeating letters return -1. Words will be separated by spaces. 
"""
def LetterCount(str_input):
    s = str_input.split(" ")
    repeat_num = []
    for word in s:
        table = {}
        for letter in word:
	    if letter.isalpha():
	        if letter in table:
		    table[letter] = table.get(letter)+1
		else:
		    table[letter] = 1
        repeat_num.append(max(table.values()))
    
    if max(repeat_num) == 1:
        return -1
    else: 
        return s[repeat_num.index(max(repeat_num))]
print LetterCount("Hello apple pie")	    
print LetterCount("Hello apple pie")
