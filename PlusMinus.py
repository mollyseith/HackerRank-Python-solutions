#Plus Minus
#Input: first line contains integer, n, denoting size of the array. Second line contains n space-seperated integers describing array of numbers
#Constraints: 0<n<100 -100<=arr[i]<=100
#Output: 1, decimal representing fraction of positive numbers compared to its size
#2, decimal representing fraction of negative numbers compared to its size
#3, decimal representing fraction of zeros compared to its size

from __future__ import division

n = int(raw_input())
ary = map(int, raw_input().split())

p=0
l=0
z=0

for i in range(n):
    if ary[i]>0:
        p = p + 1
    elif ary[i]<0:
        l = l + 1
    else:
        z = z + 1
    
print "{:.6f}".format(p/n)
print "{:.6f}".format(l/n)
print "{:.6f}".format(z/n)
