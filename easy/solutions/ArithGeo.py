def ArithGeo(arr_input):
    if len(arr_input) <= 2:
        print "Please input an array including three numbers at least"
    else: 
        const_sub = arr_input[1] - arr_input[0]
        const_div = arr_input[1] / arr_input[0]
  
        if all(const_sub == arr_input[i] - arr_input[i-1] for i in range(2,len(arr_input))):
            return "Arithmetic"
        elif all(const_div == arr_input[i] / arr_input[i-1] for i in range(2,len(arr_input))):
            return "Geometric"
        else:
            return -1
    
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print ArithGeo([1,3,9,27])
print ArithGeo([2,4,6, 8])
print ArithGeo([1,25,4,9])

