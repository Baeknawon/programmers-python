def solution(diffs, times, limit):
    max_level = max(diffs) #최대 diff로 숙련도 설정해두기
    start = 1
    end = max_level
    answer = max_level
    
    while start < end:
        level = int((start + end) / 2) #정수여야함
        time = times[0] #첫번째 문제를 푸는 시간으로 설정
        
        
        for i in range(1, len(diffs)):
            k = 0
            if level < diffs[i]: #숙련도가 부족할 경우(문제를 못풂)
                k = diffs[i] - level
            time += (times[i] + times[i-1]) * k + times[i]
            
        if time <= limit: #제한시간 안에 다 풀었을 경우
            end = level
            answer = level
        else: # 현재 level 로 못 풀었기 때문에 하나 증가시켜서 실행
            start = level + 1
    return answer