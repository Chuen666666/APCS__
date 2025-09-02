a,b = map(int,input().split())
n= int(input())
x = list(map(int,input().split()))
s = int(0)

for i in range(n):
    紅綠燈= a+b
    c=int(x[i]) % (紅綠燈)
    if (c >= a) :
        s=s+(紅綠燈-c)
print(s)