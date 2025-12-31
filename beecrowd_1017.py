# ----------------------------------------------------------
# Programa: Cálculo de consumo de combustível
# Descrição:
# Joaozinho deseja calcular quantos litros de combustível
# são gastos em uma viagem.
#
# O automóvel percorre 12 km por litro.
# Para o cálculo, são informados:
#  - Tempo da viagem (em horas)
#  - Velocidade média (em km/h)
#
# A partir disso:
# 1) Calculamos a distância percorrida
# 2) Calculamos o consumo de combustível
# 3) Exibimos o resultado com 3 casas decimais
# ----------------------------------------------------------

# Entrada de dados 
tempo = int(input("Tempo: "))
velocidade = int(input("Velocidade: "))


# Calculando a distância percorrida
distancia =  (tempo * velocidade)

# Consumo fixo por litro 
consumo = 12

# Cálculo da quantidade de litros necessários
litros = ( distancia / consumo )

# Exibição do resultado
print(f'{litros:.3f}')