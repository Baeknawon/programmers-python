while True:
    a,b,c = map(int,input().split())
    if a ==0 and b ==0 and c ==0:
        break
    num = [a,b,c]
    num.sort()
    if num[0] + num[1] <= num[2]:
        print('Invalid')
    else:
        if num[0] == num[1] == num[2]:
            print('Equilateral')
        elif num[0] == num[1] or num[1] == num[2] or num[0] == num[2]:
            print('Isosceles')
        else:
            print('Scalene')
    