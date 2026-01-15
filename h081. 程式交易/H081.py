n, D = map(int, input().split())
a = list(map(int, input().split()))

x = a[0]
profit = 0
sell_price = 0
has_stock = True

for i in range(1, n):
    if a[i] >= x + D and has_stock:
        profit += a[i] - x
        has_stock = False
        sell_price = a[i]
    if a[i] <= sell_price - D and not has_stock:
        x = a[i]
        has_stock = True

print(profit)
