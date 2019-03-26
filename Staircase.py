#Staircase
#Input: a single integer, n, denoting the size of the staircase
#Constraints: 0<=n<=100
#Output: print a staircase of size n using # symbols and spaces

n = int(raw_input())
for stairs in range(1, n + 1):
    print ' ' * (n - stairs) + '#' * stairs
