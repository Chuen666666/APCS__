a, b, c = map(int, input().split())
n = False
a, b, c = bool(a), bool(b), bool(c)

if (a and b) == c:
    print('AND')
    n = True
if (a or b) == c:
    print('OR')
    n = True
if (a ^ b) == c:
    print('XOR')
    n = True
if not n:
    print('IMPOSSIBLE')
