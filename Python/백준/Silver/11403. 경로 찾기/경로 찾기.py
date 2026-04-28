import sys
input = sys.stdin.readline
M = int(input())
path = []
for _ in range(M):
    path.append([int(x) for x in input().split()])
for k in range(M): #중간 노드부터 검사해야 나중에 따다닥 다 연결가능
    for i in range(M):
        for j in range(M):
            if path[i][k] == 1 and path[k][j] == 1: 
                path[i][j] = 1
for row in path:
    print(' '.join(map(str,row)))