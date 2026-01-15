n, d = map(int, input().split())
money = 0
c = 0

for _ in range(n):
    price = list(map(int, input().split()))
    if max(price) - min(price) >= d:
        c += 1
        money += sum(price) // 3

print(c, money)
