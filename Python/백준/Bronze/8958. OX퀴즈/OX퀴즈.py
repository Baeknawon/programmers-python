T = int(input())
for _ in range(T):
    ox = str(input())
    arr = list(ox)
    arr2 = []
    cnt = 0
    for i in range(0,len(arr)):
        if arr[i] == 'O':
            cnt += 1
            arr2.append(cnt)
        else:
            cnt = 0
            arr2.append(cnt)
    total = sum(arr2)
    print(total)    
    
        
                
        