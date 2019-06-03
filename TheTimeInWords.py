#The Time In Words
#Input: the first line contains h, the hours. The second line contains m, the minutes.
#Constraints: 1 <= h <= 12, 0 <= m <= 60
#Output: print the time in words as described

#!/bin/python3

import sys

h,m=int(input()),int(input())

nums =['','one','two','three','four','five','six','seven',
       'eight','nine','ten','eleven','twelve','thirteen','fourteen',
       'quarter','sixteen','seventeen','eighteen','nineteen', 'twenty',
       'twenty one', 'twenty two', 'twenty three', 'twenty four', 'twenty five',
       'twenty six', 'twenty seven', 'twenty eight', 'twenty nine']
if m == 0:
    print(nums[h] + ' o\' clock')
elif m > 30:
    if m == 45:
        print('quarter to ' + nums[h + 1])
    else:
        print(nums[(60 - m)] + ' minutes to ' + nums[h + 1])
elif m < 30:
    if m == 1:
        print(nums[m] + ' minute past ' + nums[h])
    if m == 15:
        print('quarter past ' + nums[h])
    else:
        print(nums[m] + ' minutes past ' + nums[h])
else:
    print('half past ' + nums[h])
