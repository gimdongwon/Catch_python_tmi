n = int(input())

card_list = list(map(int, input().split()))

m = int(input())

arr = list(map(int, input().split()))

result =""

for item in arr:
    if item in card_list:
        result += str(item) + " "

print(result)