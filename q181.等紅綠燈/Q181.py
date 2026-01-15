a, b = map(int, input().split())
n = int(input())
x = list(map(int, input().split()))
s = 0

for i in range(n):
    traffic_light = a + b
    c = int(x[i]) % (traffic_light)
    if c >= a:
        s += traffic_light - c
print(s)
