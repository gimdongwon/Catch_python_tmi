# 김동원 페이지

## 알게된 점

### 1. defaultDict, dict 차이

defaultDict는 새롭게 키를 지정할 떄 초기값을 제공한다.

```python3
d = dict()
names = ["Lee", "James", "John", "Smith", "Lee", "James"]
for name in names:
    # d에 name이 있는지 확인하고 값을 넣어주어야 에러가 발생하지 않음!
    if name in d:
        d[name] += 1
    else:
        d[name] = 1
```

이게 싫다면

```python3
from collections import defaultDict

d = defaultDict(int)
names = ["Lee", "James", "John", "Smith", "Lee", "James"]
for name in names:
    d[name] += 1
```

이렇게 하면 가능하다.

### 2. Chain

```python3
from itertools import chain
a = [1,2,3]
b = [3,2]

c = [a,b] # [[1,2,3],[3,2]]
d = list(chain(*c))

print(d) # [1,2,3,3,2]
```

### 3. extends

```python3
a = [1,2,3]
b = [3,2]

a.extend(b) # [1,2,3,3,2]
```

### 4. Counter

리스트에서 원소들의 갯수를 세어줌.

```python3
from collections import Counter

a = [1,2,3,3,2]
counter = Counter(a)
print(counter)
# Counter({2:2, 3:2, 1:1})
```
