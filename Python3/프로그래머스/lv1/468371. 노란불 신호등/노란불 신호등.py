import math
def solution(signals):
    cycles = []
    for signal in signals:
        cycles.append(sum(signal))
        
    #주기들의 최소공배수 계산(여기까지만 계산하면 됨)
    lcm = 1
    for num in cycles:
        lcm = lcm * num // math.gcd(num,lcm)
        
    #1초부터 최소공배수 시각까지만 확인
    for time in range(1,lcm+1):
        yellow = True #전부 다 노란색이면 True, 하나라도 다른색이면 False, for문 나오기
        
        for g,y,r in signals: #행 하나에 들어있는 초노빨 
            cycle = g + y + r
            now = (time - 1) % cycle + 1
            
            if not (g + 1 <= now <= g + y): #노란불이 아니라면
                yellow = False
                break
        #모든 불이 노란불이면 시간 반환
        if yellow == True:
            return time
        
    return -1
    
    
        