# Este script demonstra como exibir diferentes tipos de dados de saída em Python.

nome = "João"
idade = 25

# --- Formatando a saída com f-strings ---
print(f"Olá, {nome}! Você tem {idade} anos.")

# --- Usando múltiplos argumentos em print ---
print("Nome:", nome, "Idade:", idade)

# --- Controlando a quebra de linha ---
print("Esta frase", end=" ")
print("continua na mesma linha.")

# --- Imprimindo com separador personalizado ---
print("1", "2", "3", sep="-")  # Saída: 1-2-3
