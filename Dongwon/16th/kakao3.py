def solution (n,k,cmd):
    selected = k
    deleted = []
    up = [-1] + [i for i in range(n-1)]
    down = [i for i in range(1, n)] + [-1]
    exists = [True for _ in range(n)]
    
    for item in cmd:
        if len(item) >= 2:
            direction, score = item.split(" ")
            score = int(score)
            if direction == "U":
                for _ in range(score):
                    selected = up[selected] # point
            else:
                for _ in range(score):
                    selected = down[selected]
        else:
            if item == "Z":
                d = deleted.pop()
                if up[d] != -1:
                    down[up[d]] = d # point
                if down[d] != -1:
                    up[down[d]] = d
                exists[d] = True
            else:
                if up[selected] != -1:
                    down[up[selected]] = down[selected] # point
                if down[selected] != -1:
                    up[down[selected]] = up[selected]
                    
                exists[selected] = False
                deleted.append(selected)
                selected = down[selected] if down[selected] != -1 else up[selected]
                
    return "".join(list(map(lambda x: "O" if x else "X", exists)))