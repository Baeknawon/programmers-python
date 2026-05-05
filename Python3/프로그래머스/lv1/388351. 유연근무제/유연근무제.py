def solution(schedules, timelogs, startday):
    deadline = [] #출근가능한 최대시간
    answer = [1] * len(schedules)
    for i in range(len(schedules)):
        h = schedules[i] // 100
        m = schedules[i] % 100
        m += 10
        if m >= 60:
            h += 1
            m -= 60
        deadline.append(h * 100 + m)
    for i in range(len(schedules)):
        for j in range(7):
            if (startday + j) % 7 == 6 or  (startday + j) % 7 == 0: #토, 일이 아닐때만 카운트  
                continue
            if deadline[i] < timelogs[i][j]:
                answer[i] = 0
                break
    answer = answer.count(1)        
    return answer