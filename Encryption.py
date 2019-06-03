#Encryption
#Input: one line of text, string s
#Constraints: 1 <= s <= 81, s is comprised only of chars in range ascii[a-z]
#Output: print the encoded message on one line as described

import math

s = list(input().strip())
L =  len(s)
row = math.floor(L**(1/2))
col = math.ceil(L**(1/2))

for i in range(col):
    x = 0     
    while True:
        try:
            print(s[i+x],end='')
            x+= col
        except:
            break        
    print(' ',end='')
