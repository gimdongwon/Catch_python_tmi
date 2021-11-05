# 1차 시도 replace 이용

import re

while True:
    bracket = input().rstrip()

    bracket = re.sub("[^\(\)\[\]]", "", bracket)

    stack = []
    flag = True

    for i in bracket:
        if i == "(" or i == "[":
            stack.append(i)
        elif i == "]":
            if stack and stack[-1] == "[":
                target = stack.pop()
            else:    
                flag = False
                break
        elif i == ")":
            if stack and stack[-1] == "(":
                target = stack.pop()
            else:
                flag = False
                break
    if bracket == ".":
        break
    if flag and stack:
        print("yes")
    else:
        print("no")

# 2차 시도

while True:
    bracket = input().rstrip()

    stack = []
    flag = True

    for i in bracket:
        if i == "(":
            stack.append("(")
        elif i == "[":
            stack.append("[")
        elif i == "]":
            if stack and stack[-1] == "[" :
                stack.pop()
            else:
                flag = False
                break
        elif i == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                flag = False
                break

    if bracket == ".":
        break
    if flag and not(stack):
        print("yes")
    else:
        print("no")