N = int(input())

students = []

for __ in range(N):
     name, lang, math, eng = input().split(" ")
     students.append([name, int(lang), int(math), int(eng)])

students.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for item in students:
    print(item[0])