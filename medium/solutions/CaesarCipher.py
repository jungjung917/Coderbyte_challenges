def CaesarCipher(str,num):
    str_out = ""
    list_letter = "abcdefghijklmnopqrstuvwxyz"
    for letter in str:
        if letter.lower() in list_letter:
	    if list_letter.index(letter.lower()) + num > 25:
	        str_out = str_out + chr(ord(letter)-25+num) 
	    else: 
	        str_out = str_out + chr(ord(letter) + num) 
        else:
	    str_out = str_out + letter
    return str_out
print CaesarCipher("Hello",4)
print CaesarCipher("abcz", 0)
