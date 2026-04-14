N = int(input())
arr = [list(input()) for _ in range(N)]

heartX, heartY = 0, 0
found = False

# 심장 찾기 (0-based로 저장)
for i in range(N):
    for j in range(N):
        if arr[i][j] == '*':
            heartX, heartY = i+1, j   
            found = True
            break
    if found:
        break

# 왼쪽 팔
leftArm = 0
for i in range(heartY - 1, -1, -1):   
    if arr[heartX][i] == '*':         
        leftArm += 1
    else:
        break

# 오른쪽 팔
rightArm = 0
for i in range(heartY + 1, N):        
    if arr[heartX][i]:                
        if arr[heartX][i] == '*':
            rightArm += 1
        else:
            break

# 허리
waist = 0
for i in range(heartX + 1, N):        
    if arr[i][heartY] == '*':         
        waist += 1
    else:
        waistX = i - 1
        waistY = heartY
        break

# 왼쪽 다리
leftLeg = 0
for i in range(waistX + 1, N):
    if arr[i][waistY - 1] == '*':
        leftLeg += 1
    else:
        break

# 오른쪽 다리
rightLeg = 0
for i in range(waistX + 1, N):
    if arr[i][waistY + 1] == '*':
        rightLeg += 1
    else:
        break

# 출력 (여기서만 +1)
print(heartX + 1, heartY + 1)
print(leftArm, rightArm, waist, leftLeg, rightLeg)