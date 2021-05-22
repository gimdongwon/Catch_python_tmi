N = input()
fear_list = list(map(int, input().split(" ")))
fear_list.sort()
max_fear = fear_list[0] # fear_list 중에서 최솟값
count = 0
result = 0

for fear in fear_list:    
    if count == 0:
        count = fear
    
    count -= 1
    
    if fear > max_fear:
        count = fear - (max_fear - count)
        max_fear = fear
        
    if count == 0:
        result += 1

print(result)