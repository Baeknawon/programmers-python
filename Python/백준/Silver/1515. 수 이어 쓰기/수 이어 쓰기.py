import sys

num = sys.stdin.readline().rstrip()
n = 0 #뒤에서 문자열로 변경해서 받아야됨
idx = 0
while True:
    n+=1
    for s in str(n): #n 문자열 변경해서 자리별로 숫자 비교
        if num[idx] == s:
            idx +=1
            if idx >= len(num):
                print(n)
                exit()
            
        
    