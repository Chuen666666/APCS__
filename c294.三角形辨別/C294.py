a=sorted(map(int,input().split()))

for i in range(3):
    if(i<2) :
        print(a[i],end=" ")
    else :
        print(a[i])
if a[0]+a[1]<=a[2] :
    print("No")
elif a[0]*a[0]+a[1]*a[1]==a[2]*a[2]:
    print("Right")
elif a[0]*a[0]+a[1]*a[1]>a[2]*a[2] :
    print("Acute")
elif a[0]*a[0]+a[1]*a[1]<a[2]*a[2] :
    print("Obtuse")