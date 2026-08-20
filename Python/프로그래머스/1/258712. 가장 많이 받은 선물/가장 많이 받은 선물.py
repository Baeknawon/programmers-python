def solution(friends, gifts):
    answer = [0] * len(friends)
    table = [[0 for _ in range(len(friends))] for _ in range(len(friends))] #주고받은 선물 저장하는 테이블
    giftnum = [0] * len(friends) #선물지수 저장
    #선물 지수 계산, 테이블에 주고 받은 숫자까지 계산해서 넣기
    for gift in gifts:
        give, take = gift.split() #공백으로 나눠서 저장
        give_index , take_index = friends.index(give), friends.index(take)
        giftnum[give_index] += 1
        giftnum[take_index] -= 1
        table[give_index][take_index] += 1
    for i in range(len(friends)):
        for j in range(i + 1, len(friends)): #중앙 대각선을 r기준으로 반만 비교하면 됨(대칭)
            if table[i][j] > table[j][i]:
                answer[i] += 1
            elif table[i][j] < table[j][i]:
                answer[j] += 1
            else:
                if giftnum[i] > giftnum[j]:
                    answer[i] += 1
                elif giftnum[i] < giftnum[j]:
                    answer[j] += 1
        
    return max(answer)