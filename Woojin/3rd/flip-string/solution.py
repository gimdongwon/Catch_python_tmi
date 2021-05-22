S = input()

zeros_freq = 0 # 연속된 0을 하나의 그룹으로 볼 때, 그 그룹의 개수
ones_freq = 0 # 연속된 1을 하나의 그룹으로 볼 때, 그 그룹의 개수

# --- 예시 ---
# S = "000110000" 일 때,
# ones_freq 는 2 ("000" 과 "0000") 
# zeros_freq 는 1 ("11")

for i, char in enumerate(S):
    if i == 0:
        if char == "0":
            zeros_freq += 1
        else:
            ones_freq += 1
    else:
        if char == "0" and S[i - 1] == "1":
            zeros_freq += 1
        elif char == "1" and S[i - 1] == "0":
            ones_freq += 1
            
print(min(zeros_freq, ones_freq))