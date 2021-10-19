word = input()

croatia_words = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for item in croatia_words:
    word = word.replace(item, "1")
    
print(len(word))
