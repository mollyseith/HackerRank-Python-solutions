#Birthday Cake Candles
#Input: first line contains integer, n, denoting number of candles on the cake, second line contains n space-seperated integers, each int i describes height of candle i
#Constraints: 1<=n<=10^5 1<=ar[i]<=10^7
#Output: print the number of candles to be blown out on a new line

n = int(raw_input())
a = map(int,raw_input().strip().split())
max_height = max(a)
matching = sum([a[i]==max_height for i in xrange(n)])
print matching
