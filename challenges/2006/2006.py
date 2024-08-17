T = input()
respostas = input().split()
numVencedores = 0
for _ in range(0, len(respostas)):
    if respostas[_] == T:
        numVencedores+=1
print(numVencedores)
