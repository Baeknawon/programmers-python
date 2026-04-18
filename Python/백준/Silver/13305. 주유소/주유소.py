#그리디 알고리즘
N = int(input())
road = list(map(int,input().split()))
price = list(map(int,input().split()))
min_price = price[0]
total = 0
for i in range(N-1): #마지막 도시 제외
    min_price = min(min_price,price[i])
    total += min_price * road[i]
print(total)