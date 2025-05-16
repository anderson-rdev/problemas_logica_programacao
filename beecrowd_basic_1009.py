# 💼 Calculadora de Comissão de Vendedor

# Este projeto em Python calcula o salário final de um vendedor com base no seu salário fixo e nas vendas realizadas durante o mês, incluindo uma comissão de 15%.

## 📋 Descrição

# O programa:

# 1. Lê o nome do vendedor.
# 2. Lê o salário fixo do vendedor.
# 3. Lê o valor total de vendas realizadas no mês.
# 4. Calcula a comissão de 15% sobre o valor das vendas.
# 5. Soma o salário fixo com a comissão e imprime o total a receber.

# Leitura de Dados
name   = str(input(''))
salary = float(input())
vendas = float(input())

# Calculando percentual de 15% sob vendas + o salário fixo do vendedor
salario_com_bonus = (vendas * 0.15) + salary

# Exibindo salário com bonificação
print(f'TOTAL = R$ {salario_com_bonus:.2f}')
