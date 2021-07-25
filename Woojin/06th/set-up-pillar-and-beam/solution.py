def can_retain(result):
    for x, y, structure in result:
        # 기둥
        if structure == 0: 
            if y == 0 or [x, y - 1, 0] in result or [x, y, 1] in result or [x - 1, y, 1] in result:
                continue
            return False
        # 보
        else: 
            if [x, y - 1, 0] in result or [x + 1, y - 1, 0] in result:
                continue
            elif [x - 1, y, 1] in result and [x + 1, y, 1] in result:
                continue
            return False
    
    return True

def solution(n, build_frame):
    result = []
    
    for build in build_frame:
        # 설치
        if build[3] == 1: 
            result.append(build[:3])
            if not can_retain(result):
                result.pop()
        # 삭제
        else: 
            result.remove(build[:3])
            if not can_retain(result):
                result.append(build[:3])

    return sorted(result)