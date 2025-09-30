a = int(input())
scores = sorted(map(int, input().split()))

for i in range(a):
    print(scores[i], end="")
    if i < a - 1:
        print(" ", end="")
print()

for i in range(a):
    if scores[a-1] < 60:
        print(scores[a-1])
        print("worst case")
        break
    elif scores[0] >= 60:
        print("best case")
        print(scores[0])
        break
    elif scores[i] >= 60:
        print(scores[i-1])
        print(scores[i])
        break