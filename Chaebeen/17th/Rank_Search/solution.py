# 순위 검색
# 정확성 O, 효율성 X
# info, query 정보만 자르기
# 쿼리가 지원자 정보에 포함되는지 확인
def solution(info, query):
    applicants = []
    qualifications = []

    answer = []

    for i in info:
        applicants.append(i.split(' '))

    for q in query:
        nq = list(filter(None, q.replace('and ', '').replace('-', '').split(' ')))
        qualifications.append(nq)

    for nq in qualifications:
        cnt = 0
        q_str = set(nq[:-1])
        q_num = int(nq[-1])
        for a in applicants:
            if set(a).issuperset(q_str) and q_num <= int(a[-1]):
                cnt += 1
        answer.append(cnt)

solution(["java backend junior pizza 150",
          "python frontend senior chicken 210",
          "python frontend senior chicken 150",
          "cpp backend senior pizza 260",
          "java backend junior chicken 80",
          "python backend senior chicken 50"],
         ["java and backend and junior and pizza 100",
          "python and frontend and senior and chicken 200",
          "cpp and - and senior and pizza 250",
          "- and backend and senior and - 150",
          "- and - and - and chicken 100",
          "- and - and - and - 150"])
