import math
import os
import random
import re
import sys


def timeConversion(s):
    # Write your code here
    hour = int(s[0:2])
    minute = s[3:5]
    second = s[6:8]
    time_period = s[8:10]
    if time_period == "PM" and hour != 12:
        hour += 12 #If its 12:01:00PM return 12:01:00 otherwise add 12 to make it 24hr
    elif time_period == "AM":
        if hour == 12:
            # If its 12:01:00AM Return 00:01:00
            hour = "00" 
        elif hour < 10 and hour > 0:
            hour = "0" + str(hour) #Add the 0 back for numbers <10 as integer conversion removes it
            # E.g 09:01:00
        # Otherwise return the the regular AM time without AM at end
    return str(hour) + ":" + minute + ":" + second
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
