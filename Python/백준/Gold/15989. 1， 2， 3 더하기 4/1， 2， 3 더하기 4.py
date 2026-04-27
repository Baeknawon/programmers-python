T = int(input())

dp = [1] * 10001 #전부 1로 구성되어있는 경우의 수  를 디폴트로 깔고감 
#인덱스 0에도 1이 있는 이유? dp[0] + dp[2], dp[0] +dp[3] 처럼 아무것도 안더 하고 2와 3으로만 이루어져있는 경우를 나타내기 위해
for i in range(2,10001):
    dp[i] += dp[i-2] #2가 더해지는 경우를 더하기 위해 2만큼 작은 수의 경우의 수를 더해줌
for i in range(3,10001):
    dp[i] += dp[i-3] #이번엔 3

for _ in range(T):
    n = int(input())
    print(dp[n])