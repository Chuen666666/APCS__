a = input()
b = 0
c = 0

for i in range(len(a)):
    if i % 2 == 0:
        b += int(a[i])
    else:
        c += int(a[i])

print(abs(c - b))
