# BEE 1012 - Área

# Lê três valores de ponto flutuante (A, B e C)
A, B, C = map(float, input().split())

# Define o valor de pi
pi = 3.14159

# Calcula as áreas
triangulo = (A * C) / 2
circulo = pi * C ** 2
trapezio = ((A + B) * C) / 2
quadrado = B ** 2
retangulo = A * B

# Exibe os resultados com 3 casas decimais
print(f"TRIANGULO: {triangulo:.3f}")
print(f"CIRCULO: {circulo:.3f}")
print(f"TRAPEZIO: {trapezio:.3f}")
print(f"QUADRADO: {quadrado:.3f}")
print(f"RETANGULO: {retangulo:.3f}")