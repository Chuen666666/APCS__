a = input()
b = int(0)
c = int(0)
for i in range(len(a)):
    if i%2==0:
        b=b+int(a[i])
    else:
        c=c+int(a[i])
   
print(abs(c-b)) #ads 是絕對值