n = int(input())
h = list(map(int, input().split()))
ans = 1
c = 1

for i in range(1, n):
    if h[i] <= h[i-1]:
        c += 1
    else:
        c = 1
    ans = max(ans, c)

print(ans)