#Minimum Loss
#Input: first line contains integer n, number of years of house data. Second line contains n
#space-seperated long integers describing each price[i]
#Constraints: 2 <= n <= 2*10^5, 1 <= price[i] <= 10^16, all prices are distinct, valid answer exists
#Output: single integer denoting minimum amt of money Lauren must lose if she buys and resells
#the house within the next n years

#!/bin/python3

import sys

n =  int(input().strip())
numbers = list(map(int,input().strip().split()))
myDict = {}
for i in range(n):
    myDict[numbers[i]]=i
smallest = 10**10
nums = sorted(myDict)
for i in range(1,n):
    if (nums[i]-nums[i-1] < smallest)  and (myDict[nums[i]] < myDict[nums[i-1]]):
        smallest = nums[i]-nums[i-1]
print(smallest)
