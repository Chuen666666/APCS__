x = int(input())
best_attact = int(0)
best_defence = int(0)
second_attact = int(0)
second_defence = int(0)

for i in range(x):
    attact,defence = map(int,input().split())
    if (attact**2)+(defence**2)>(best_attact**2)+(best_defence**2):
        second_attact = best_attact
        second_defence = best_defence
        best_attact = attact
        best_defence = defence
    elif (attact**2)+(defence**2)>(second_defence**2)+(second_attact**2):
        second_attact = attact
        second_defence = defence
print(f"{second_attact} {second_defence}")
