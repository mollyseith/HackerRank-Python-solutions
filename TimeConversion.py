#Time Conversion
#Input: string s containing a time in 12-hour format
#Constraints: all input times are valid
#Output: convert and print the given time in a 24-hour format

t = raw_input()
if t[-2:] == "AM" and t[:2] == "12": 
    print "00" + t[2:-2]   
elif t[-2:] == "AM": 
    print t[:-2] 
elif t[-2:] == "PM" and t[:2] == "12": 
    print t[:-2]        
else: 
    print str(int(t[:2]) + 12) + t[2:8]
