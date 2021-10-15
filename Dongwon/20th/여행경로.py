# T 1 : [["ICN", "B"], ["B", "ICN"], ["ICN", "A"], ["A", "D"], ["D", "A"]]
# ans : ["ICN", "B", "ICN", "A", "D", "A"]

# T 2: [["ICN", "AAA"], ["ICN", "AAA"], ["ICN", "AAA"], ["AAA", "ICN"], ["AAA", "ICN"]]
# ans : ["ICN", "AAA", "ICN", "AAA", "ICN", "AAA"]

# T 3 : [["ICN", "COO"], ["ICN", "BOO"], ["COO", "ICN"], ["BOO", "DOO"]]
# ans : ["ICN", "COO", "ICN", "BOO", "DOO"]

# 4번 반례 해결하니 2번 테케 통과했습니다.
# T 4: [["ICN", "SFO"], ["SFO", "ICN"], ["ICN", "SFO"], ["SFO", "QRE"]]
# ans : ["ICN", "SFO", "ICN", "SFO", "QRE"]

# 가장 골치아픈 1번테케는 5번반례 해결후 통과했습니다.
# T 5 : [["ICN", "BOO"], ["ICN", "COO"], ["COO", "DOO"], ["DOO", "COO"], ["BOO", "DOO"], ["DOO", "BOO"], ["BOO", "ICN"], ["COO", "BOO"]]
# ans : ["ICN", "BOO", "DOO", "BOO", "ICN", "COO", "DOO", "COO", "BOO"]

# 1차 시도.

def solution(tickets):
    start = "ICN"
    result = []
    answer = 0
    while answer < 5 and len(tickets):
        target = list(filter(lambda x: x[0] == start, tickets))
        target.sort()
        start = target[0][1]
        
        if answer == 0:
            result.extend(target[0])
        else:
            result.append(start)
        
        tickets.remove(target[0])
        answer += 1
        print(target, " WW ",tickets, "@@", start)
    return result