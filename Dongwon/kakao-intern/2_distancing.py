def solution(places):
    result = []
    dx = [-2,-1,-1,-1,0,0,0,0,1,1,1,2]
    dy = [0,-1,0,1,-2,-1,0,1,2,-1,0,1,0]
    for place in places:
        candiates = []
        wall_checklist = []
        for x in range(5):
            for y in range(5):
                cur_position = place[x][y]
                if cur_position == "P": # 응시자 선출
                    candiates.append((x,y))
        # 응시자들끼리 거리 비교
        break_point = False
        for i in range(len(candiates)):
            for j in range(i+1, len(candiates)):
                manhaton_x = candiates[i][0] - candiates[j][0]
                manhaton_y = candiates[i][1] - candiates[j][1]
                manhaton = abs(manhaton_x) + abs(manhaton_y)
                # 맨하탄 거리가 2이하일때
                if manhaton < 3:
                    if manhaton_x == 0: # x 값이 같을 때
                        if place[candiates[i][0]][(candiates[i][1] + candiates[j][1]) // 2] != "X":
                            result.append(0)
                            break_point = True
                            break
                    elif manhaton_y == 0: # y 값이 같을 때
                        if place[(candiates[i][0] + candiates[j][0]) // 2][candiates[i][1]] != "X":
                            result.append(0)
                            break_point = True
                            break
                    else:
                        # x,y 값이 다를 때
                        if place[candiates[i][0]][candiates[j][1]] != "X" or place[candiates[j][0]][candiates[i][1]] != "X":
                            result.append(0)
                            break_point = True
                            break
            if break_point: # 하나라도 맞으면 나머지는 볼 필요 없음.
                break
        else: # 거리두기 잘 지키고 있을 때
            result.append(1)
    return result