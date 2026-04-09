list = []
def pointDown(point):
    point += 1
    print('1',end='')
    return(point)

def ChannelUp(point):
    if point > 0:
        list[point] , list[point -1] = list[point -1], list[point]
        point -= 1
        print('4',end='')
    return(point)
N = int(input())
for _ in range(N):
    list.append(input())
point = 0
while True:
    if list[point] !='KBS1':
        point = pointDown(point)
    else:
        point = ChannelUp(point)
    if list[0] == 'KBS1':
        break
while True:
    if list[point] != 'KBS2':
        point = pointDown(point)
    else:
        point = ChannelUp(point)
    if list[1] == 'KBS2':
        break