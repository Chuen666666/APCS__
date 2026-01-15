n = int(input())
high = -1
times = 0
error = 0

for _ in range(n):
    ti, si = map(int, input().split())
    if si > high:
        high = si
        times = ti
    elif si < 0:
        error += 1

total = max(0, high - n - error * 2)
print(total, times)
