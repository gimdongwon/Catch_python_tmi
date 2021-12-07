def solution(enroll, referral, seller, amount):
    result = dict()
    sell_cnt = dict()
    recommander = dict()
    result["-"] = 0
    for i in range(len(enroll)):
        recommander[enroll[i]] = referral[i]
        result[enroll[i]] = 0
    
    def share(name, price):
        if name == "-" or price // 10 == 0:
            result[name] += price
            return
        money = price // 10
        mine = price - money
        result[name] += mine
        share(recommander[name], money)
    
    for i in range(len(seller)):
        name, price = seller[i], amount[i] * 100
        share(name, price)
    
    del result["-"]
    
    return list(map(int, result.values()))