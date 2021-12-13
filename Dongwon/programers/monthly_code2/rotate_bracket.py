def check(s):
    bracket_dict = {
        "]": "[",
        "}": "{",
        ")": "("
    }
    result = []
    for item in s:
        if item == "[" or item =="(" or item == "{":
            result.append(item)
        else:
            if len(result) == 0:
                return False
            temp = result.pop()
            if bracket_dict[item] != temp:
                return False
    if len(result) != 0:
        return False
    else:
        return True

def solution(s):
    result = 0
    for i in range(len(s)):
        if check(s[i:] + s[:i]):
            # print(s[i:] + s[:i])
            result += 1
    return result