import sys
N,K = map(int,sys.stdin.readline().split())
list = list(input())
cnt = 0
for i in range(len(list)):
    if list[i] == 'P':
        for j in range(i-K,i+K+1):
            if 0<= j < N and list[j] == 'H':
                cnt += 1
                list[j] = '0'
                break #첫번째 for문으로 돌아감

print(cnt)   
    