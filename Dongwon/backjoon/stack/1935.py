n = int(input())
operators = input()

numbers = [0] * n
for i in range(n):
    numbers[i] = int(input())

stack = []

for item in operators:
    
    if item.isalpha():
        stack.append(numbers[ord(item) - ord('A')])
    else:
        num2 = stack.pop()
        num1 = stack.pop()
        if item == "+":
            stack.append(num1 + num2)
        elif item == "-":
            stack.append(num1 - num2)
        elif item == "*":
            stack.append(num1 * num2)
        elif item == "/":
            stack.append(num1 / num2)

print(format(stack[0], ".2f"))