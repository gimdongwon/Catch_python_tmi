from itertools import product

n,m = map(int, input().split())

arr = [i for i in range(1, n+1)]

for item in product(arr,repeat=m):
    temp = ''
    for jtem in item:
        if len(item) == 1:
            print(jtem)
        else:
            temp += str(jtem) + ' '
    if len(item) != 1:
        print(temp.rstrip())