from collections import Counter
T = int(input())
for _ in range(T):
    N = int(input())
    runner = list(map(int,input().split()))
    team = max(runner)
    for i in range(1,team+1):
        if runner.count(i) < 6:
            while i in runner:
                runner.remove(i)
    newteam = list(dict.fromkeys(runner))#순서 유지, 중복 제거
    score =[[]for _ in range(len(newteam))]
    for i in range(len(runner)):
        rank = i + 1
        score[newteam.index(runner[i])].append(rank)

    result = sorted(
    [(newteam[i], score[i]) for i in range(len(newteam))],
    key=lambda x: (sum(x[1][:4]), x[1][4]))
    print(result[0][0])

    
    
        
    
    