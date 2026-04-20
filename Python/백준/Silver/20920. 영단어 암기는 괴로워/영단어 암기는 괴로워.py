import sys
N,M =map(int,sys.stdin.readline().split())
d = {}
for i in range(N):
    word = sys.stdin.readline().rstrip()
    if (len(word) < M):
        continue #길이가 M 보다 짧으면 건너뛰기
    if (word in d):
        d[word] += 1
    else: #단어 집어넣기 (딕셔너리에)
        d[word] = 1
#정렬은 우선순위 반대로 해야됨
d = sorted(d.items(), key = lambda x : x[0]) #알파벳 순 오름차순 여기서 리스트(튜플이됨)
d = sorted(d, key = lambda x : len(x[0]), reverse = True) #길이순 내림차순
d = sorted(d, key = lambda x : x[1],reverse = True) #빈도수대로 내림차순

for i in d:
    print(i[0])