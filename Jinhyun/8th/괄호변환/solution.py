def solution(p):
    # 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다.
    if p == "":
        return ""
    # 2. 문자열 w를 u, v로 분리
    u = ""
    v = ""
    counter = 0
    for p_val in p:
        if p_val == "(":
            counter += 1
        else:
            counter -= 1
        u += p_val
        if counter == 0:
            v = p[len(u) :]
            u_correct = True
            if u[0] == ")":
                u_correct = False
            # 3. 문자열 u가 올바른 괄호 문자열이라면
            if u_correct:
                return u + solution(v)
            # 4. 문자열 u가 올바른 괄호 문자열이 아니라면
            else:
                # 4-1, 4-2, 4-3
                new = "(" + solution(v) + ")"
                # 4-4
                new_u = ""
                for i in u[1:-1]:
                    if i == "(":
                        new_u += ")"
                    else:
                        new_u += "("
                return new + new_u


print(solution("()))((()"))
