def solution(letters, k):
    n_deleted = len(letters) - k
    stack = []
    
    for char in letters:
        while n_deleted and stack and stack[-1] < char:
            n_deleted -= 1
            stack.pop()

        stack.append(char)
         
    return "".join(stack[:k])