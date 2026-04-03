while True:
    A = int(input())
    if A == -1:
        break
    arr = []
    for i in range(1,A):
        if A % i == 0:
            arr.append(i)
    if sum(arr) == A:
        print(A, " = ", " + ".join(str(i) for i in arr), sep="")
    else:
        print(A,"is NOT perfect.")
        