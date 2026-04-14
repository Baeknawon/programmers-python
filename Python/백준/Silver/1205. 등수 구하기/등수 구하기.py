N, T, P = map(int, input().split())

if N: #N이 0이 아닐때
    arr = list(map(int, input().split()))
else:
    arr = []

# 리스트 꽉 찼고, 꼴등보다 작거나 같으면 불가능
if N == P and T <= arr[-1]:
    print(-1)
else:
    arr.append(T)
    arr.sort(reverse=True)
    print(arr.index(T) + 1)