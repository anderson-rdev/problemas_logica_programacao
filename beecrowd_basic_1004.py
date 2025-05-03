# Leia dois valores inteiros. A seguir, calcule o produto entre estes dois valores e atribua esta operação à variável PROD. A seguir mostre a variável PROD com mensagem correspondente.

# Entrada
# O arquivo de entrada contém 2 valores inteiros.

 # Saída
 # Imprima a mensagem "PROD" e a variável PROD conforme exemplo abaixo, com um
 # espaço em branco antes e depois da igualdade. Não esqueça de imprimir o fim
 # de linha após o produto, caso contrário seu programa apresentará a mensagem:
 # “Presentation Error”.

# Criando Função
def product_new(a, b):
    # Calculando o Produto entre os números
    prod = (a * b)
    return prod

#Leitura de Dados
a = int(input())
b = int(input())

# Chamada da função para soma dos valores
prod = product_new(a, b)

# Imprimindo o resultado
print(f'PROD = {prod}')

