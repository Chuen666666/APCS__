for i in range(int(input())):
    Q = []
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    if not (a[1] != a[3] and a[1] == a[5] and b[1] != b[3] and b[1] == b[5]):
        Q.append("A")
    if not (a[6] == 1 and b[6] == 0):
        Q.append("B")
    if not (a[1] != b[1] and a[3] != b[3] and a[5] != b[5]):
        Q.append("C")
    if not Q:
        print(None)
    else:
        print(*Q, sep="")