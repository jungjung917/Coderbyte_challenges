def CaesarCipher(str,num):
    str_out = ""
    list_letter = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if num == 0:
        return str
    else:
        for letter in str:
            if letter in list_letter:
	        if letter.lower() == 'z':
	            str_out = str_out + list_letter[list_letter.index(letter)-25+num] 
	        else: 
	            str_out = str_out + list_letter[list_letter.index(letter) + num] 
            else:
	        str_out = str_out + letter
    return str_out
print CaesarCipher("Hello",4)
print CaesarCipher("abcz", 0)
