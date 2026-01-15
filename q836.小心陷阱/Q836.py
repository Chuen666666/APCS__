k = int(input())
place = 0

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())

while place > 0:
    place += k
    if place % x1 == 0:
        k -= y1
    if place % x2 == 0:
        k -= y2

print(place)
