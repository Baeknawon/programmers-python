import math
N = int(input())
M = int(input())
x = list(map(int,input().split()))
gap = []
gap.append(x[0])
for i in range(1,M):
     gap.append(math.ceil((x[i] - x[i-1])/2))
gap.append(N - x[-1])
print(max(gap))
