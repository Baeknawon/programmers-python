#브루트포스 알고리즘(무식하게 다 구함)
N = int(input())
body = [list(map(int,input().split()))for _ in range(N)] #[[],[],,,]
for i in range(N):
    cnt = 0
    for k in range(i+1,N):
        if body[i][0] < body[k][0] and body[i][1] <body[k][1]:
            cnt +=1
    for j in range(i-1,-1,-1):
        if body[i][0] < body[j][0] and body[i][1] < body[j][1]:
            cnt +=1
    print(cnt+1,end=' ')