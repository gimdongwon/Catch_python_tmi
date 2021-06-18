# 현재 건축물의 상태 확인
def check_status(result):
    for x,y,stuff in result:
        # 확인 대상이 기둥일 시
        if stuff == 0:
            # 맨 아래가 바닥이거나, 아래가 보 이거나, 아래가 기둥이면 진행
            if y == 0 or [x-1,y,1] in result or [x,y,1] in result or [x,y-1,0] in result:
                continue
        # 확인 대상이 보 일시
        else:
            # 아래가 기둥이거나, 오른쪽 아래가 기둥이거나, 양옆이 보 일시 진행
            if [x,y-1,0] in result or [x+1,y-1,0] in result or ([x-1,y,1] in result and [x+1,y,1] in result):
                continue
        return True
    return False

def solution(n, build_frames):
    result = []
    for build_frame in build_frames:
        x,y,a,b = build_frame
        result_format = [x,y,a]
        # 삭제 일시
        if b == 0:
            result.remove(result_format)
            if check_status(result):
                result.append(result_format)
        # 설치 일시
        else:
            result.append(result_format)
            if check_status(result):
                result.remove(result_format)
    return sorted(result)