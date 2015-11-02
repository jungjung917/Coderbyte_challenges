def LetterChanges(str): 
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    vowels = "aeiou"
    str_replace = ""
    for index, letter in enumerate(str):
        print index
	if letter in letters:
	    if letter.lower() == 'z':
                str = str[:index] + chr(ord(letter)-25) + str[index+1:]
            else:
                str = str[:index] + chr(ord(letter) + 1) + str[index+1:]
        print str      
  
    for index,letter in enumerate(str):
        if letter in vowels:
	    str =  str[: index] + letter.upper() +  str[index+1:]
 
    return str
# keep this function call here  
# to see how to enter arguments in Python scroll dohello*3")
print  LetterChanges("a bcdefghijklmnopqrstuvwxyz123")
