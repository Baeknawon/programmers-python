def solution(bandage, health, attacks):
    end = attacks[-1][0]
    seq = 0
    now = health
    i = 0
    for sec in range(end+1):
        if sec != attacks[i][0]: #공격을 안받을때
            seq += 1
            now += bandage[1]
            if seq == bandage[0]: #연속 공격 성공
                now += bandage[2]
                seq = 0
            if now > health:
                now = health
            if now <= 0:
                return -1
        if i < len(attacks) and sec == attacks[i][0]: #공격 받을 때 시간 sec
            seq = 0
            now -= attacks[i][1]
            i += 1
            if now <= 0:
                return -1
    
    return now