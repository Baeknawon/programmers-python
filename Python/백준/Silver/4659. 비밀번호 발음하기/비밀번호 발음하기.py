while True:
    pwd = input()
    if pwd == 'end':
        break
    #조건 1 검열
    #if 'a' in pwd or 'e' in pwd or 'i' in pwd or 'o' in pwd or 'u' in pwd:
    if not any(c in pwd for c in 'aeiou'): #조건 1 불만족, 출력하고 다음 패스워드로
        print(f"<{pwd}> is not acceptable.")
        continue #아래코드 실행 안하고 while문으로
    #조건 2 검열
    ok = True #조건 판단 기준
    for i in range(len(pwd)-2):
        if pwd[i] in ('aeiou') and pwd[i+1] in ('aeiou') and pwd[i+2] in ('aeiou'): #조건 2 불만족
            ok = False
            break #for문 밖으로
        if pwd[i] not in ('aeiou') and pwd[i+1] not in ('aeiou') and pwd[i+2] not in ('aeiou'): #조건 2 불만족
            ok = False
            break #for문 밖으로
    if not ok: #조건 2가 불만족이라면
        print(f"<{pwd}> is not acceptable.")
        continue #아래코드 실행 안하고 while문으로
    #조건 3 검열
    for i in range(len(pwd)-1):
        if pwd[i] == pwd[i+1] and pwd[i] not in ('eo'):#조건 3불만족
            ok = False
            break
    if not ok: #조건 2가 불만족이라면
        print(f"<{pwd}> is not acceptable.")
        continue #아래코드 실행 안하고 while문으로
    #조건 3개 다 통과시
    print(f"<{pwd}> is acceptable.")
            
    
    
    
                
        