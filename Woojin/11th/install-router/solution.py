# --- 백준 스타일 ---

from sys import stdin

def get_mid(homes, start, end):
    mid = (start+end) // 2
    mean = (homes[start]+homes[end]) // 2
    
    if homes[mid] > mean:
        while homes[mid] > mean:
            mid -= 1
        
        if mean - homes[mid] > homes[mid + 1] - mean:
            mid += 1
    else:
        while homes[mid] <= mean:
            mid += 1
        
        if homes[mid] - mean > mean - homes[mid - 1]:
            mid -= 1
    
    return mid

N, C = map(int, input().split())
homes = []

for _ in range(N):
    homes.append(int(stdin.readline()))

homes.sort()
start = 0
end = N - 1
C -= 2

if C == 0:
    print(homes[end] - homes[start])
else:
    mid = get_mid(start, end)
    C -= 1
    
    if C == 0:
        print(min(homes[end] - homes[mid], homes[mid] - homes[start]))
    else:
        if homes[end] - homes[mid] > homes[mid] - homes[start]:
            mid = get_mid(homes, mid, end)
            C -= 1

while C > 0:
    mid = get_mid(start, end)
while start <= end:
    if C == 0:
        break
    
    mid = get_mid(homes, start, end)   
    C -= 1
    