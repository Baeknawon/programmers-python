#import sys
#input = sys.stdin.readline
T = int(input())
for _ in range(T):
    n,k,t,m = map(int,input().split())
    ranking =  []
    for _ in range(n): 
        ranking.append([0,0,[0 for _ in range(k)]]) #각 팀 별 시도 횟수, 시간, 문제 별 점수 저장
    for time in range(m):
        i,j,s = map(int, input().split())
        ranking[i-1][0] += 1 #해당 팀 번호 - 1 = 인덱스, 해당 팀의 제출 횟수 증가
        ranking[i-1][1] = time # 마지막 제출 시간 저장 (순서가 곧 제출시간임)
        ranking[i-1][2][j-1] = max(s,ranking[i-1][2][j-1]) #문제 번호 j의 최고 점수 저장
    totalScore = [0] * n
    for i in range(n):
        totalScore[i] = sum(ranking[i][2]) #문제의 점수 총 합
    #등수 계산 최종점수 비교
    teams = []
    for i in range(n): #팀번호, 최종점수, 제출 횟수, 마지막 제출 시간 순서로 sort
        teams.append((i+1,totalScore[i], ranking[i][0], ranking[i][1]))
    teams.sort(key=lambda x : (-x[1],x[2],x[3])) #최종점수 내림차순, 횟수 오름, 시간 오름
    for i in range(len(teams)):
        if teams[i][0] == t:
            print(i+1)
            break