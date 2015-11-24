def LongestWord(string)
  string = string.gsub(/[^A-Za-z0-9\s]/i, '')
  puts string
  str_arr = string.split(" ")
  len_arr = []
  str_arr.each {|word| len_arr << word.length }
  
  return str_arr[len_arr.index(len_arr.sort[-1])]
end

puts LongestWord("This is not true, I can believ!e it@@g$rdf")
