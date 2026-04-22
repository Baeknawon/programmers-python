#슬라이딩 윈도우
import sys
input = sys.stdin.readline
N,X = map(int,input().split())
visitor = list(map(int,input().split()))
total = []
window_sum = sum(visitor[:X])
total.append(window_sum)
for i in range(X,N):
    window_sum += visitor[i]
    window_sum -= visitor[i-X]
    total.append(window_sum)
#print(total)
max = max(total)
if max == 0:
    print('SAD')
else:
    cnt = total.count(max)
    print(max)
    print(cnt)
    