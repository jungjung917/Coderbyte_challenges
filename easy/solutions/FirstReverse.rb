=begin
Have the function FirstReverse(str) take the str parameter being passed and return the string in reversed order. 
=end
#!/usr/bin/ruby
def FirstReverse(str_in)
    str_new = String.new("")
   str_in.each_char {|letter| str_new = letter + str_new}
    return str_new
end
puts FirstReverse("abcd")
