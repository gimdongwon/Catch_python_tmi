n = int(input())

# print(bin(n)[2:])

def find_bin(x):
    if x == 0:
        return
    else:
        find_bin(x//2)
        print(x%2, x)

find_bin(n)