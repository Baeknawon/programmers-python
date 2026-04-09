T = int(input())
for _ in range(T):
    U = int(input())
    n = []
    S = []
    for _ in range(U):
        name,s = input().split()
        s = int(s)
        n.append(name)
        S.append(s)
    print(n[S.index(max(S))])
        
    
    