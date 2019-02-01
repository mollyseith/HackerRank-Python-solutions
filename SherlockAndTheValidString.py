#!/bin/python3
#Input: a single string s
#Constraints: 1 <= |s| <= 10^5, each character s[i] set of ascii[a-z]
#Output format: print YES if string s is valid, otherwise, print NO

from collections import Counter
 
s = raw_input()
characters = Counter(s)
character_counter = Counter(characters.values())
 
if len(character_counter) == 1:
    return True
 
if len(character_counter) == 2:
    for i in character_counter.values():
        if i == 1:
            return True
 
return False
