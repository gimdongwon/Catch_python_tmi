import heapq

def solution(operations):
    result = [0,0]
    max_que = []
    min_que = []
    queue = []
    
    for operation in operations:
        commend,number = operation.split(" ")
        # 숫자 추가
        if commend == "I":
            number = int(number)
            heapq.heappush(queue, number)
        # 숫자 삭제
        else:
            target = 0
            #  최댓값 삭제
            if number == "1":
                for i in range(len(queue)):
                    queue[i] = -queue[i]
                if len(queue)>0:
                    heapq.heappop(queue)
                for i in range(len(queue)):
                    queue[i] = -queue[i]
            # 최솟값 삭제
            else:
                if len(queue)>0:
                    heapq.heappop(queue)
    if queue == []:
        return [0,0]
    else:
        min_num = heapq.heappop(queue)
        max_num = max(queue)
        return [max_num, min_num]