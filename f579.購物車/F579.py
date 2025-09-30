a, b = map(int, input().split())
n = int(input())
ans = 0

for i in range(n):
    x = map(int, input().split())
    c = [0] * 101
    for k in x:
        if k > 0:
            c[k] += 1
        elif k < 0:
            k = -k
            c[k] -= 1
    if c[a] > 0 and c[b] > 0:
        ans += 1

print(ans)