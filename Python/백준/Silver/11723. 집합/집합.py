S = set()
def add(S,num):
    S.add(num)
def remove(S,num):
    S.discard(num)
    
def check(S,num):
    print(1 if num in S else 0)
def toggle(S,num):
    if num not in S:
        S.add(num)
    else:
        S.discard(num)
def all():
    return set(range(1,21))
def empty():
    return set()
import sys
input = sys.stdin.readline
N = int(input())
for _ in range(N):
    cmd = input().split()
    if cmd[0] == 'add':
        add(S,int(cmd[1]))
    elif cmd[0] == 'remove':
        remove(S,int(cmd[1]))
    elif cmd[0] == 'check':
        check(S,int(cmd[1]))
    elif cmd[0] == 'toggle':
        toggle(S,int(cmd[1]))
    elif cmd[0] == 'all':
        S = all()
    elif cmd[0] == 'empty':
        S = empty()
        
        
    
    