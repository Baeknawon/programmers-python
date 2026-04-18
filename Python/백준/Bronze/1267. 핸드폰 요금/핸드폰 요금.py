N = int(input())
time = list(map(int,input().split()))
totalY, totalM = 0,0
for i in range(len(time)):
    Y = 10
    M = 15
    Y = Y + 10 * (time[i] // 30)
    totalY += Y
    M = M + 15 * (time[i] // 60)
    totalM += M
if totalY < totalM:
    print('Y',totalY)
elif totalY > totalM:
    print('M',totalM)
else:
    print('Y M',totalY)