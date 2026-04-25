import sys
N,M = map(int,sys.stdin.readline().split())
list = [list(map(int,sys.stdin.readline().split())) for _ in range (N)]
costs = []
dx = [-1,0,1] #좌우
dy = [1,1,1] #밑으로만
def dfs(x,y,direct,cost): #재귀로 표현
    if y == N-1: #끝까지 닿으면 (더 깊이갈 곳이 없으면)
        costs.append(cost) #비용 저장
        return
    for i in range(3):
        if i == direct: continue #아래 실행 안함 왜? -> 같은 방향 연속인지 체크
        nx ,ny = x + dx[i] , y + dy[i]
        if(-1 < nx < M) and (-1 < ny < N):
            dfs(nx,ny,i,cost + list[ny][nx])
for i in range(M):
    dfs(i,0,-1,list[0][i]) #방향 왼쪽 대각선 아래부터 시작
print(min(costs))
    