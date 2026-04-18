from collections import deque
N = int(input())
queue = deque()
for i in range(1,N+1):
    queue.append(i)
while len(queue) > 1:
    queue.popleft() #왼쪽 빼기(삭제)
    queue.append(queue.popleft()) #왼쪽 빼서 오른쪽에 append
print(queue[0])
    