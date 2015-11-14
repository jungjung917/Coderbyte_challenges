"""
Using the Python language, have the function LetterCountI(str) take the str parameter being passed and return the first word with the greatest number of repeated letters. For example: "Today, is the greatest day ever!" should return greatest because it has 2 e's (and 2 t's) and it comes before ever which also has 2 e's. If there are no words with repeating letters return -1. Words will be separated by spaces. 
"""
def LetterCountI(str_input):
  s = str_input.split(" ")
  letter_list = []
  for index, word in enumerate(s):
      
      letter_count = 1
      letter_table = {} 
      for letter in word.lower():
          if letter in letter_table.keys():
              letter_count += 1
	      letter_table[letter] = letter_count
          else:
              letter_table[letter] = 1
      letter_list.insert(index, max(letter_table.values()))
  if max(letter_list) == 1:
      return -1
  else:
      return s[letter_list.index(max(letter_list))]
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print LetterCountI("Hello apple pie")  


