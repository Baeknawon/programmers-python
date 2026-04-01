mem = int(input())
s = str(input())
arr = list(s)
A = arr.count('A')
B = arr.count('B')
if A > B:
    print('A')
elif A < B:
    print('B')
else:
    print('Tie')