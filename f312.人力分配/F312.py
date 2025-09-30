A1, B1, C1 = map(int, input().split())
A2, B2, C2 = map(int, input().split())
n = int(input())
ans = -float('inf')

for i in range(n+1):
    X1 = i
    X2 = n - i
    Y1 = A1*X1**2 + B1*X1 + C1
    Y2 = A2*X2**2 + B2*X2 + C2
    ans = max(ans, Y1+Y2)

print(ans)