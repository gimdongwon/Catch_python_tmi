# --- 백준 스타일 ---

N = int(input())
transcript = []

for _ in range(N):
    name, kor, eng, math = input().split()
    transcript.append([name, int(kor), int(eng), int(math)])

# 국어 내림차순
# 영어 오름차순
# 수학 내림차순
# 이름 오름차순

transcript.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for name, *_ in transcript:
    print(name)