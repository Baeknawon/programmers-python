N,K = map(int,input().split())
medal = [list(map(int,input().split())) for _ in range(N)] #전부다 배열에 넣음
medal.sort(key = lambda x : (x[1],x[2],x[3]),reverse = True) #금은동 많은 순대로 내림차순 정렬
idx = [medal[i][0] for i in range(N)].index(K) # 알고싶은 K 국가의 인덱스(몇번째인지) 구하기
for i in range(N):
    if medal[idx][1:] == medal[i][1:]:
        print(i+1) #정렬된 위치 기반으로 등수 결정
        break