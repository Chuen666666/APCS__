a = sorted(map(int, input().split()))

if a[0] == a[1] == a[2]:
    print(f"3 {a[0]}")
elif a[0] == a[1] or a[0] == a[2] or a[1] == a[2]:
    print(f"2 {max(a)} {min(a)}")
else:
    print(f"1 {a[-1]} {a[-2]} {a[-3]}")

# [another solution]
# from collections import Counter

# a = list(map(int, input().split()))
# c = Counter(a)

# print(max(c.values()), end=" ")
# for i in sorted(c.keys(), reverse=True):
#     print(i, end=" ")