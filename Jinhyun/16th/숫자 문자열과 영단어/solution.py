def solution(s):
    number_word = {'zero' : 0, 'one' : 1, 'two' : 2, 'three' : 3, 'four' : 4,
                  'five' : 5, 'six' : 6, 'seven' : 7, 'eight' : 8, 'nine' : 9}
    s_list = []
    word = ''
    for i in s :
        try :
            s_list.append(int(i))
        except :
            word += i
        if word in number_word :
            s_list.append(number_word[word])
            word = ''
    s_len = len(s_list)
    answer = 0
    for i in s_list :
        answer += i * 10 ** (s_len - 1)
        s_len -= 1
    return answer