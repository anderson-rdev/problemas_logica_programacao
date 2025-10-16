# Entrada de dados 
distancia = int(input())
litros = float(input())

# Calculo médio de consumo por km rodado 
consumo = ( distancia / litros ) 

# Imprimindo retorno
print(f'{consumo:.3f} km/l')