from collections import defaultdict,Counter
import sys

input = sys.stdin.readline

n = int(input())

card_list = Counter(list(map(int, input().split())))

m = int(input())

arr = list(map(int, input().split()))
print(arr)
arr = set(arr)
print(arr)

result = ""

for item in arr:
    result += str(card_list[item]) + " "

print(result)