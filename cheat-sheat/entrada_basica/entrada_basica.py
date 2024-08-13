# Este script demonstra como ler diferentes tipos de dados de entrada em Python.

# --- Lendo uma linha inteira como string ---
linha = input()
print(linha)

# --- Lendo um inteiro ---
inteiro = int(input())
print(inteiro)

# --- Lendo um número de ponto flutuante ---
flutuante = float(input())
print(flutuante)

# --- Lendo uma lista de inteiros ---
inteiros = list(map(int, input().split()))
print(inteiros)

# --- Lendo uma lista de floats ---
flutuantes = list(map(float, input().split()))
print(flutuantes)

# --- Lendo múltiplas entradas em uma linha ---
palavra1, palavra2 = input().split()
print(palavra1, palavra2)

# --- Lendo um número finito e conhecido de linhas ---
n = int(input())  # Lê o número de linhas a serem lidas

for _ in range(n):
    linha = input()  # Lê cada linha
    print(linha)
    # ... processa a linha


# --- Lendo uma matriz de inteiros ---
n, m = map(int, input().split())  # Lê as dimensões da matriz

matriz = []
for _ in range(n):
    linha = list(map(int, input().split()))
    matriz.append(linha)

print(matriz)

# --- Lendo um número finito e desconhecido de linhas ---
while True:
    try:
        linha = input()
        print(linha)
        # ... processa a linha
    except EOFError:
        break
