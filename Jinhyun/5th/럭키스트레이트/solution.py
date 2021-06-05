# -*- coding: utf-8 -*-
# 럭키스트레이트의 특정조건
# 현재 캐릭터 점수 N (항상 짝수)
# 자리수 기준 반으로 나누어 왼쪽 자리수 합과 오른쪽 자리수 합이 같을 경우 사용 가능
# 사용 가능시 "LUCKY"
# 사용할 수 없다면 "READY"

def solution(first_line) :
    length = len(first_line) // 2
    left = list(map(int, first_line[:length]))
    right = list(map(int, first_line[length:]))
    if sum(left) == sum(right) :
        return "LUCKY"
    else :
        return "READY"

print(solution("123402"))
print(solution("7755"))