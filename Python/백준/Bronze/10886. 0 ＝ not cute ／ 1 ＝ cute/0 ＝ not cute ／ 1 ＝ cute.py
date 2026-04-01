T = int(input())
arr = []
for _ in range(T):
    a = int(input())
    arr.append(a)
zero = arr.count(0)
one = arr.count(1)
if zero > one:
    print('Junhee is not cute!')
elif zero < one:
    print('Junhee is cute!')