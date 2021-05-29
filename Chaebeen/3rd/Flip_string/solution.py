def string_flip(s):
    result = 1
    for i in range(len(s)-1):
        if s[i] != s[i+1]:
            result += 1
    return result // 2


print(string_flip("0001100"))
