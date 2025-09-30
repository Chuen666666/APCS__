a, b, c = sorted(map(int, input().split()))

for i in range(3):
    if i < 2:
        print(a[i], end=" ")
    else:
        print(a[i])

if a + b <= c:
    print("No")
elif a**2 + b**2 == c**2:
    print("Right")
elif a**2 + b**2 > c**2:
    print("Acute")
else:
    print("Obtuse")