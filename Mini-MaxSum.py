#Mini-Max Sum
#Input: a single line of five space-seperated integers
#Constraints: 1<=arr[i]<=10^9
#Output: two space-seperated long integers denoting minimum and maximum values that can be calculated by summing exactly four or the five integers (output can be greater than 32 bit integer)

a = map(int, raw_input().strip().split())  

a.sort()
tot = sum(a)
print(tot - a[-1]), (tot - a[0])
