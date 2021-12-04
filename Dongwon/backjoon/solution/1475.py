import math
from collections import Counter

s = input()

s = s.replace('6', '9')

result = Counter(s)

result['9'] /= 2
print(int(math.ceil(result.most_common(1)[0][1])))