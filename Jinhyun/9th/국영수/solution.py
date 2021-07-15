from collections import defaultdict

def solution(n, classes):
    name_dict = defaultdict()
    for i in classes.split('     ') :
        name = ''
        k_e_m = []
        for j in i.split() :
            try :
                if isinstance(int(j), int) :
                    k_e_m.append(int(j))
            except :    
                name = j
            name_dict[name] = k_e_m
    name_dict = sorted(name_dict.items(), key=lambda x : (-x[1][0], x[1][1], -x[1][2], x[0]))
    for sort_name in name_dict :
        print(sort_name[0])



solution(
    12,
    "Junkyu 50 60 100 \
    Sangkeun 80 60 50 \
    Sunyoung 80 70 100 \
    Soong 50 60 90 \
    Haebin 50 60 100 \
    Kangsoo 60 80 100 \
    Donghyuk 80 60 100 \
    Sei 70 70 70 \
    Wonseob 70 70 90 \
    Sanghyun 70 70 80 \
    nsj 80 80 80 \
    Taewhan 50 60 90"
)
