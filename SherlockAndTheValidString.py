#!/bin/python3
#Input: a single string s
#Constraints: 1 <= |s| <= 10^5, each character s[i] set of ascii[a-z]
#Output format: print YES if string s is valid, otherwise, print NO

import collections

s = raw_input().strip()
freq = collections.Counter(s)
values = list(freq.values())
values.sort()
print('YES' if values.count(values[0]) == len(values) or (values.count(values[0]) == len(values) - 1 and values[-1] - values[-2] == 1) or (values.count(values[-1]) == len(values) - 1 and values[0] == 1) else 'NO')
