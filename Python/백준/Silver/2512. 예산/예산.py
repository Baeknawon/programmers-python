def binary(arr,start,end,M):
    global result
    if start > end:
        return
    else:
        mid = (start + end) //2 #상한선값
        total = 0
        for i in arr:
            if i > mid: #상한선값보다 크면 상한선값
                total += mid
            else:
                total += i
        if total <= M: #합이 전체 값보다 작으면..? 상한선을 올려도 된다는 의미
            result = mid
            return binary(arr,mid+1,end,M)
        else:
            return binary(arr,start,mid-1,M)
    
N = int(input())
lst = list(map(int,input().split()))
M = int(input())
start,end = 1,max(lst)
result = 0
binary(lst,start,end,M)
print(result)
