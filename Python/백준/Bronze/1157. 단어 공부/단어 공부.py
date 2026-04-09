word = list(input().upper())
arr = list(set(word))
cnt = []
for i in range(len(arr)):
    count = word.count(arr[i])
    cnt.append(count)
if cnt.count(max(cnt)) > 1:
    print('?')
else:
    print(arr[cnt.index(max(cnt))])
    