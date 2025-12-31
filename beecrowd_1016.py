# ----------------------------------------------------------
# Programa: Distância entre dois carros
# Descrição:
# Dois carros (X e Y) partem na mesma direção.
#
# - Carro X: velocidade constante de 60 km/h
# - Carro Y: velocidade constante de 90 km/h
#
# A diferença de velocidade entre eles é de 30 km/h,
# o que significa que o carro Y se afasta 1 km a cada
# 2 minutos em relação ao carro X.
#
# O programa deve:
# 1) Ler a distância (em km)
# 2) Calcular o tempo necessário (em minutos)
# 3) Exibir o tempo seguido da palavra "minutos"
# ----------------------------------------------------------

# Entrada de dados
distancia = int(input(""))

# Diferença de velocidade 
diferenca_velocidade = 30 

# Cálculo do tempo necessário em minutos
velocidade_por_minuto = ( diferenca_velocidade / 60 )
tempo = distancia / velocidade_por_minuto

# Exibindo resultado
print(f"{int(tempo)} minutos")