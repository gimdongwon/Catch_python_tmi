# 누적합

## 1차 시도

def solution(triangle):
    result = []
    def dfs(idx, target_idx, total):
        # print(total, idx, target_idx)
        # print(result)
        if idx == len(triangle) - 1:
            return total
        idx += 1
        temp = total
        total += triangle[idx][target_idx]
        # if dfs(idx, target_idx, total) != None:
        result.append(dfs(idx, target_idx, total))
        total = temp
        total += triangle[idx][target_idx+1]
        # if dfs(idx, target_idx+1, total) != None:
        result.append(dfs(idx, target_idx+1, total))
        # if triangle[idx][target_idx] > triangle[idx][target_idx+1]:
        #     total += triangle[idx][target_idx]
        #     return dfs(idx, target_idx, total)
        # else:
        #     total += triangle[idx][target_idx+1]
        #     return dfs(idx, target_idx+1, total)
    dfs(0,0,triangle[0][0])
    print(len(result))
    # return max(result)
    # return answer

## 2차 시도