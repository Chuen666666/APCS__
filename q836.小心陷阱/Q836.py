k = int(input())
place = 0 

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())

for _ in range(99):
    place += k 
    if place % x1 == 0:
        k = k - y1
    if place % x2 == 0:
        k = k - y2
    if k <= 0:
        print(place)
        break