pipe = list(input())
# pipe = list("()(((()())(())()))(())")
# pipe = list("(((()(()()))(())()))(()())")
stack = []

result = 1

for i in range(len(pipe)-1):
    if pipe[i] == "(":
        stack.append("(")
    else:
        stack.pop()
        if pipe[i-1] == "(":
            result += len(stack)
        else:
            result += 1

print(result)