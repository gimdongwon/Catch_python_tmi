def solution (n,k,cmd):
    selected = k
    stack = []
    board = [i+1 for i in range(n)]
    arr = [1 for _ in range(n)]
    for item in cmd:
        # print(item)
        # print(arr, selected, stack)
        if len(item) == 3:
            direction, score = item.split(" ")
            temp = 0
            if direction == "U":
                while temp < int(score) and selected >= 0:
                    selected -= 1
                    temp += arr[selected]
            else:
                while temp < int(score) and selected <= n-1:
                    selected += 1
                    temp += arr[selected]
        else:
            if item == "Z":
                if stack:
                    garbage = stack.pop()
                    arr[garbage] = 1
            else:
                arr[selected] = 0
                stack.append(selected)
                if selected < n-1:
                    selected += 1
                    while arr[selected] == 0:
                        selected += 1
                        if arr[selected] != 0:
                            break
                else:
                    selected -= 1
                    while arr[selected] == 0:
                        selected -= 1
                        if arr[selected] != 0:
                            break
                # 기본은 +1 증가인데 다음 노드가 없으면 다음으로 맨 마지막 노드이면 그전 노드로
    return "".join(list(map(lambda x: "O" if x==1 else "X", arr)))