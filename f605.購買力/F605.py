n,d = map(int,input().split())
money = int(0)
c = int(0)
for i in range (n):
    price = list(map(int,input().split()))
    if max(price) - min(price) >=d :
        c += 1 
        money += sum(price)//3 
print(c,money)