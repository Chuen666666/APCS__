times = int(input())
w1, w2, h1, h2 = map(int, input().split())
ans = 0
x = list(map(int, input().split()))

for i in range(len(x)):
    added = 0
    while h1 > 0 and x[i] > 0:
        added += 1
        h1 -= 1
        x[i] -= w1**2
    while h2 > 0 and x[i] > 0:
        added += 1
        h2 -= 1
        x[i] -= w2**2
    ans = max(ans, added)
    
print(ans)