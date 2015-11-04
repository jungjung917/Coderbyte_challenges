def AlphabetSoup(str): 
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    #letter_order = list()
    letter_order = dict()
    str_ordered = ""
  
    for index,letter in enumerate(str):
    #    print alphabets.index(letter.lower())
        if letter.lower() in alphabets:
  
            letter_order[index] = alphabets.index(letter.lower())
    #letter_order.sort()
    letter_order_sorted = sorted(zip(letter_order.values(),letter_order.keys()))

    for i in range(0,len(letter_order_sorted)):
        str_ordered = str_ordered + str[letter_order_sorted[i][1]]
    return str_ordered
    
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print AlphabetSoup("ADFHgtuyuua")     
