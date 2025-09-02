a,b,c=map(int,input().split())
n = int(0)
a,b,c = bool(a),bool(b),bool(c)
if( a and b )== c:
    print("AND")
    n+=1 
if (a or b) == c:
    print("OR")
    n+=1 
if (a ^ b) == c:
    print("XOR")
    n+=1 
if n == 0:
    print("IMPOSSIBLE")