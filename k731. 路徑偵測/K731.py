n = int(input())
a, b = map(int, input().split())
next = 0
now = 0
# 東0 北1 西2 南3
left = right = turn = nothing = 0

for _ in range(n - 1):
    x, y = map(int, input().split())
    if x > a:
        next = 0
    elif x < a:
        next = 2
    if y > b:
        next = 1
    elif y < b:
        next = 3
    if now == next:
        nothing += 1
    elif next - now == 1 or next - now == -3:
        left += 1
    elif next - now == 2 or next - now == -2:
        turn += 1
    elif next - now == 3 or next - now == -1:
        right += 1
    now, a, b = next, x, y

print(left, right, turn)
