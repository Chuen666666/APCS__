n = int(input())
a,b = map(int,input().split())
準備方向=0
現在方向=0
#東 0 北1 西2 南 3 
L,R,T,Nothing = 0,0,0,0
for i in range(n-1):
    x,y = map(int,input().split())
    if  x > a:
        準備方向=0
    elif x < a :
        準備方向=2
    if y > b :
        準備方向=1
    elif y < b :
        準備方向=3
    if 現在方向==準備方向:
        Nothing+=1
    elif 準備方向-現在方向==1 or 準備方向-現在方向==-3:
        L+=1
    elif 準備方向-現在方向==2 or 準備方向-現在方向==-2:
        T+=1
    elif 準備方向-現在方向==3 or 準備方向-現在方向==-1:
        R+=1
    現在方向,a,b=準備方向,x,y
print(L,R,T)
    


    