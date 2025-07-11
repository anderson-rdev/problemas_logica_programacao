# Leitura de dados
salario = float(input())

def calcular_imposto(salario):
    # Calculando imposto de renda
    if salario <= 2000.00:
        return 0.00
    elif salario <= 3000.00:
        return (salario - 2000) * 0.08
    elif salario <= 4500.00:
        return (salario - 3000) * 0.18 + 1000 * 0.08
    else:
        return (salario - 4500) * 0.28 + 1500 * 0.18 + 1000 * 0.08

# Chamando função
def main():
    imposto = calcular_imposto(salario)
    if imposto > 0:
        print(f'R$ {imposto:.2f}')
    else:
        print('Isento')

if __name__ == "__main__":
    main()        
