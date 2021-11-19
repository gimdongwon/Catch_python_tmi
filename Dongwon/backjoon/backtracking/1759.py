from itertools import combinations

l,c = map(int, input().split())
alphabets = input().split()

vowels = ['a','e','i','o','u']

candidates = set(combinations(alphabets, l))
result = []
for candidate in candidates:
    temp = set(candidate)
    vowel,consult = 0,0
    for i in temp:
        if i in vowels:
            vowel+=1
        else:
            consult += 1
    if len(temp) == l and vowel >= 1 and consult > 1:
        temp = list(temp)
        temp.sort()
        temp = "".join(temp)
        if  temp not in result:
            result.append(temp)
result.sort()
for item in result:
    print(item)

