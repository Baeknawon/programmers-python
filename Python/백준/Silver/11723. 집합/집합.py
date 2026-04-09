#비트마스크
import sys
input = sys.stdin.readline

S = 0
N = int(input())
for _ in range(N):
    cmd = input().split()

    if cmd[0] == 'add':
        S |= (1 << int(cmd[1])) #cmd[1] 번째 자리에 1만들기(있다고 표시) |= -> 기존값에 합치기
    elif cmd[0] == 'remove':
        S &= ~(1 << int(cmd[1])) #cmd위치만 1로 바꾸고 반전, 그러면 cmd위치만 0(제거) 가 됨 &= -> 해당 자리만 0으로 만들기(제거)
    elif cmd[0] == 'check':
        print(1 if S & ( 1 << int(cmd[1])) else 0) #S랑 cmd[1] 이랑 비교해서 0이면 없음 1이면 있음
    elif cmd[0] =='toggle':
        S ^= (1 << int(cmd[1])) #xor임. S랑 cmd 비교,1^1 = 0(제거), 0^1 = 1(추가)
    elif cmd[0] == 'all':
        S = (1 << 21) -1 #21번째까지..100000..였는데 -1하면 1111...(다있는상태)
    elif cmd[0] =='empty':
        S = 0 #비우기