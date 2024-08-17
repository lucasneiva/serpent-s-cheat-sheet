def calcFatorial(n):
    if n == 2:
        return 2
    else:
        return n*calcFatorial(n-1)

print(calcFatorial(int(input())))