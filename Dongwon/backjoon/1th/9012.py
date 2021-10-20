n = int(input())

for _ in range(n):
    stack = 0
    bracets = list(input())
    for bracet in bracets:
        if bracet == "(":
            stack += 1
        else:
            stack -= 1
        if stack == -1:
            break
    print("YES" if stack==0 else "NO")
    
