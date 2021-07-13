# --- 프로그래머스 스타일 ---

def solution(N):
    N_list = list(map(int, N))
    half_len = len(N_list) // 2
    
    if sum(N_list[:half_len]) == sum(N_list[half_len:]):
        return "LUCKY"
    else:
        return "READY"
    
print(solution("123402"))
print(solution("931223"))

# --- 백준 스타일 ---

N_list = list(map(int, input()))
half_len = len(N_list) // 2

if sum(N_list[:half_len]) == sum(N_list[half_len:]):
    print("LUCKY")
else:
    print("READY")