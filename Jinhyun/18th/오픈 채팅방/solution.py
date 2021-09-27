from collections import defaultdict

def solution(record):
    user = defaultdict()
    answer = []
    for command in record :
        command_list = command.split()
        if command_list[0] == 'Enter' :
            user[command_list[1]] = command_list[2]
            answer.append((command_list[1], command_list[0]))
        elif command_list[0] == 'Leave' :
            answer.append((command_list[1], command_list[0]))
        else :
            user[command_list[1]] = command_list[2]
    command_list = []
    for i in answer :
        user_id, state = i
        if state == 'Enter':
            command_list.append(f"{user[user_id]}님이 들어왔습니다.")
        else :
            command_list.append(f"{user[user_id]}님이 나갔습니다.")
    return command_list