word = input()
alphabets = list('abcdefghijklmnopqrstuvwxyz')

result = ''

for alphabet in alphabets:
    if alphabet in word:    
        result += str(word.index(alphabet)) + ' '
    else:
        result += '-1 '
        
print(result)