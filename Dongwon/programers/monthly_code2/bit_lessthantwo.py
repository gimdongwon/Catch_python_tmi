def solution(numbers):
    result = []
    for number in numbers:
        bin_number = list('0' + bin(number)[2:])
        # 맨 오른쪽 0을 찾기.
        idx = ''.join(bin_number).rfind('0')
        bin_number[idx] = '1'
        
        # 홀수면 idx 다음 수를 0으로 바꾸면 답 구할수 잇음.
        if number % 2 == 1:
            bin_number[idx+1] = '0'
        result.append(int(''.join(bin_number), 2))
        
    return result