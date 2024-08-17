N = int(input())

qtdeMaxCirculos = 1;

pivo = input()

for i in range(1, N):
    numAtual = input()
    
    if (numAtual != pivo):
        qtdeMaxCirculos += 1
        pivo = numAtual

print(qtdeMaxCirculos)
