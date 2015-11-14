"""
Using the Python language, have the function CountingMinutesI(str) take the str parameter being passed which will be two times (each properly formatted with a colon and am or pm) separated by a hyphen and return the total number of minutes between the two times. The time will be in a 12 hour clock format. For example: if str is 9:00am-10:00am then the output should be 60. If str is 1:00pm-11:00am the output should be 1320. 
"""
def CountingMinutesI(str_input): 
    time_list = str_input.split("-")
    hhmm = []
    minuts=[]
    if time_list[0] == time_list[1]:
        return 0
    else:
        if time_list[0][-2:] == "am" and time_list[1][-2:] == "am":
	    for i in range(0,2):
	        if time_list[i] == "12:00am":
		    time_list[i] = "0:00am"
        for i in range(0,2):
            hhmm.append(time_list[i][:-2].split(":"))
	    minuts.append(60*int(hhmm[i][0]) + int(hhmm[i][1]) + (12*60 if time_list[i][-2:]=="pm" else 0))

	min_interval = minuts[1] - minuts[0]  
        if min_interval < 0:
	    min_interval = min_interval + 24*60
	return min_interval
print CountingMinutesI("12:30pm-12:00am")
    
