def solution(players, m, k):
    server = [0] * 24 #현재 서버 개수 저장
    cnt = 0
    time = 0
    Has_server = False
    for i in range(24):
        need = players[i] // m #필요한 서버의 개수
        if need > server[i]:
            add = need - server[i] #추가해야되눈 서버 개수
            for j in range(i ,min(i+k, 24)):
                server[j] += add
            cnt += add
            
    return cnt