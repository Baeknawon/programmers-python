def solution(n, w, num):
    box = [[]for _ in range(w)]
    reversed_state = False
    for i in range(1,n+1):
        box[(i-1)%w].append(i)
        if i % w == 0: #다 채우면 그 뒤부터 채우는 방향 바꾸기
            box.reverse()
            reversed_state = not reversed_state
            
     # 🔥 핵심: 마지막 상태가 뒤집혀 있으면 다시 원복
    if reversed_state:
        box.reverse()
    for i in range(len(box)):
        for j in range(len(box[i])):
            if box[i][j] == num:
                answer = len(box[i]) - j 
                return answer