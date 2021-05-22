S = input()

ones_freq = 0
zeros_freq = 0

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
            
print(min(ones_freq, zeros_freq))