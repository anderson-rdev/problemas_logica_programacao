# Calculadora de Salário de Funcionário

# Este programa em Python calcula o salário de um funcionário com base nas horas trabalhadas e no valor por hora.

## 💡 Descrição

# O programa realiza os seguintes passos:

# 1. Lê o número de identificação do funcionário.
# 2. Lê o número de horas trabalhadas.
# 3. Lê o valor que o funcionário recebe por hora.
# 4. Calcula o salário total.
# 5. Exibe o número do funcionário e o salário no formato especificado.

# Leitura de dados
numero = int(input())               # Número do funcionário
horas_trabalhadas = int(input())    # Total de horas trabalhadas
valor_por_hora = float(input())     # Valor Por hora 

#calculando hora
salario = numero * horas_trabalhadas

# Saída formatada
print(f'NUMBER = {numero}')
print(f'SALARY = U$ {salario:.2f}')
