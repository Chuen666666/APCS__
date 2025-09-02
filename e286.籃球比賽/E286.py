w = int(0)
for _ in range(2):
    a = sum(map(int,input().split()))
    b = sum(map(int,input().split()))
    print(f"{a}:{b}")
    if a > b :
        w+=1
if w == 2:
    print("Win")
elif w == 1:
    print("Tie")
else:
    print("Lose")
