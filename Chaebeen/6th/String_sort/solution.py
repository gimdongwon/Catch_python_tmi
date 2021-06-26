def solution(s):
    num = 0
    string = []

    for i in s:
        if ord(i) <= 57:
            num += int(i)
        else:
            string.append(i)
    string.sort()
    if num != 0:
        string.append(str(num))

    return ''.join(string)


print(solution("AJKDLSI412K4JSJ9D"))
print(solution("AJKDLSIKJSJD"))




