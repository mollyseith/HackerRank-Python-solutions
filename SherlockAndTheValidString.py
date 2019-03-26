#Sherlock and the Valid String
#Input: a single string s
#Constraints: 1 <= |s| <= 10^5, each character s[i] set of ascii[a-z]
#Output format: print YES if string s is valid, otherwise, print NO

l = list(raw_input())
alphabet = "abcdefghijklmnopqrstuvwxyz"
l1 = list()
count = 0
for i in range(26):
    temp = l.count(alphabet[i])
    if(temp != 0):
        count += 1
    l1.append(temp)
val = l1.count(l1[0])
if (val == count-1 or val == count):
    print "YES"
else:
    print "NO"
