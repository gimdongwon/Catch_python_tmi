# coding=utf-8
def split(s):
    left = 0
    right = 0
    for i in range(len(s)):
        if s[i] == '(':
            left += 1
        else:
            right += 1
        if left == right:
            return i
    return len(s)


def check(s):  # 올바른 문자열인지 체크
    pair = {')': '('}
    stack = []
    for char in s:
        if char not in pair:  # 왼쪽 괄호를 스택에 push
            stack.append(char)
        elif not stack or pair[char] != stack.pop():  # 오른쪽 괄호가 나오면 스택 pop
            return False  # 스택이 비어있거나 오른쪽 괄호가 아니라면 false
    return len(stack) == 0  # 모두 pop 되었으면 올바른 문자열


def check2(s):  # 문자열이 '(', ')'뿐이라면 pair[char] != stack.pop() 비교할 필요 없다.
    stack = []
    for char in s:
        if char == '(':  # '('를 스택에 push
            stack.append(char)
        elif stack:  # ')'를 만났을때 스택이 비어있지 않으면
            stack.pop()  # pop
        else:  # 스택이 비어있으면 false
            return False
    return len(stack) == 0


def solution(s):
    if s == "":
        return ""
    split_index = split(s)
    u = s[:split_index + 1]
    v = s[split_index + 1:]
    if check(u):
        return u + solution(v)
    else:
        result = '('
        result += solution(v)
        result += ')'
        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        return result + ''.join(u)


print(solution(")((((())))"))
print(solution("()))((()"))
