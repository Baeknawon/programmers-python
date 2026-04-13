N,play = input().split()
N = int(N)
player =[]
for _ in range(N):
    player.append(input())
player= list(set(player)) #중복 아이디 없애기

if play =='Y':
    if len(player) >= 1:
        print(len(player)//1)
    else:
        print(0)
if play =='F':
    if len(player) >= 2:
        print(len(player)//2)
    else:
        print(0)
if play =='O':
    if len(player) >= 3:
        print(len(player)//3)
    else:
        print(0)


    