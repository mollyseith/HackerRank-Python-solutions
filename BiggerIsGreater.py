#Bigger Is Greeater
#Input: first line contains T, the number of test cases. Each of next T lines contains w
#Constraints: 1 <= T <= 10^5, 1 <= |w| <= 100, w contains only letters in range ascii[a-z]
#Output: for each case, output the string meeting the criteria. If no answer exists, "no answer"

#!/bin/python3

import sys

for x in range(int(input())):
    w = input().strip()
    n = len(w)+1
    for i in range(-2,-n,-1):
        if w[i]<w[i+1]:
            print(w[:i],end='')
            v = w[:i:-1]
            for j in range(-i-1):
                if w[i]<v[j]:
                    print(v[j]+v[:j]+w[i]+v[j+1:])
                    break
            else:
                print(v+w[i])
            break
    else:
        print('no answer')
