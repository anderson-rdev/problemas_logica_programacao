# # beecrowd | 1005
# ## Média 1
# Adaptado por Neilor Tonin, URI Brasil

# Leia 2 valores de ponto flutuante de dupla precisão A e B, que correspondem a 2 notas de um aluno. A seguir, calcule a média do aluno, sabendo que a nota A tem peso 3.5 e a nota B tem peso 7.5 (A soma dos pesos portanto é 11). Assuma que cada nota pode ir de 0 até 10.0, sempre com uma casa decimal.

# ### Entrada
# O arquivo de entrada contém 2 valores com uma casa decimal cada um.

# ### Saída
# Imprima a mensagem "MEDIA" e a média do aluno conforme exemplo abaixo, com 5 dígitos após o ponto decimal e com um espaço em branco antes e depois da igualdade. Utilize variáveis de dupla precisão (double) e como todos os problemas, não esqueça de imprimir o fim de linha após o resultado, caso contrário, você receberá "Presentation Error".

# ### Exemplos de Entrada e Saída

# | Entrada | Saída          |
# |---------|----------------|
# | | MEDIA = 6.43182        |
# | 7.1     |                |
# |---------|----------------|
# | 0.0     |MEDIA = 4.84091 |
# | 7.1     |                |
# |---------|----------------|
# | 10.0    |MEDIA = 10.00000|
# | 10.0    |                |


def calculando_mediaponderada(A, B):
    peso_a = 3.5
    peso_b = 7.5
    # Calculando mC)dia ponderada
    calculo = ((A * peso_a) + (B * peso_b)) / (peso_b + peso_a)
    return calculo


# Leitura de dados
A = float(input())
B = float(input())

calculo = calculando_mediaponderada(A, B)

# Resultando Final
print(f"\nMEDIA = {calculo:.5f}")
