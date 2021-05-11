import re

def solution(new_id):
    # 1. 대문자를 소문자로 치환
    new_id = new_id.lower()
    # 2. 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자 제거
    new_id = re.sub("[^a-z0-9-_.]", "", new_id)
    # 3. 마침표(.)가 2번이상 연속된 부분은 하나의 마침표로 치환
    new_id = re.sub("[..]+", ".", new_id)
    # print(new_id)
    # 4. 마침표(.)가 처음이나 끝에 위치하면 제거
    new_id = new_id.strip(".")
    # 5. 빈문자열이면 new_id는 a로 치환
    if len(new_id) == 0:
        new_id = 'a'
    # 6. 16자 이상이면 첫 15개만 남기고 나머지 제거, 제거 후 마침표(.)가 끝에 위치하면 제거
    if len(new_id) > 15:
        new_id = new_id[0:15]
        new_id = new_id.strip(".")
    # 7. new_id의 길이가 2이하이면 마지막 문자를 총 길이가 3이 될때까지 반복
    if len(new_id) < 3:
        i = 3 - len(new_id)
        new_id = new_id + new_id[-1] * i
    print(new_id)

solution("...!@BaT#*..y.abcdefghijklm")
solution("z-+.^.")
solution("=.=")
solution("123_.def")
solution("abcdefghijklmn.p"	)
