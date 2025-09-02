n = int(input())
high = int(-1)
times = int(0)
error = int(0)
for i in range(n):
    ti,si = map(int,input().split())
    if si > high :
        high = si
        times = ti
    elif si < 0:
        error+=1
total = high - n - error*2
if total < 0:
    total = int(0)
print(total,times)