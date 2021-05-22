N = input()
fear_list = list(map(int, input().split(" "))) # 두 번째 입력값을 자연수 리스트로 만들기
fear_list.sort() # 공포도를 오름차순 정렬
max_fear = fear_list[0] # 그룹화가 진행되고 있는 그룹에서 제일 큰 공포도 (즉, 해당 그룹이 완성되기 위해 필요한 모험가 수)
remainder = 0 # 그룹화가 진행되고 있는 그룹을 완성하기 위해 필요한 모험가 수
result = 0 # 완성된 그룹 수

for fear in fear_list:
    if remainder == 0: # 필요한 모험가 수가 0 이면 새로운 그룹을 만들어야 하므로
        remainder = fear # 필요한 모험가 수를 공포도(fear)로 갱신
    
    remainder -= 1 # 루프가 진행될 때마다 모험가를 그룹화가 진행 중인 그룹에 넣는다. 
    
    if fear > max_fear: # max_fear 보다 공포도가 큰 모험가가 있다면
        remainder += fear - max_fear # remainder 를 갱신
        max_fear = fear # max_fear 를 갱신
        
    if remainder == 0: # 필요한 모험가 수가 0 이면
        result += 1 # 완성된 그룹 수에 추가

print(result)