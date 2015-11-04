""" the function PalindromeTwo(str) take the str parameter being passed and return the string true if the parameter is a palindrome, (the string is the same forward as it is backward) otherwise return the string false. The parameter entered may have punctuation and symbols but they should not affect whether the string is in fact a palindrome. For example: "Anne, I vote more cars race Rome-to-Vienna" should return true. 
"""
def PalindromeTwo(input_str):
    new_str = ""
    result = list()
    for letters in input_str:
        if letters.isalpha():
	    new_str = new_str + letters.lower()
    for i in range(0, len(new_str)/2):
        if new_str[i] != new_str[-(i+1)]:
	    result.append(False)
	else:
	    result.append(True)

    if all(result):
        return "true"
    else:
        return "false"
	
print PalindromeTwo("Anne, I vote more cars race Rome-to-Vienna")
