n,D = map(int,input().split())
a = list(map(int,input().split()))
x = a[0]
利潤 = int(0)
賣出價格 = int(0)
是否持股 = True
for i in range(1,n):
    if a[i] >= x + D and 是否持股 == True:
        利潤 += a[i] - x 
        是否持股 = False
        賣出價格 = a[i]
        
    if a[i] <= 賣出價格 - D and 是否持股 == False:
        x = a[i]
        是否持股 = True
    
print(利潤)
        