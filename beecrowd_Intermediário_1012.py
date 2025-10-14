# BEE 1012 - Área

# Lê três valores de ponto flutuante (A, B e C)
A, B, C = map(float, input().split())

# Define o valor de pi
pi = 3.14159

# Calcula as áreas
def calculotriangulo(A,C):
    retorno = (A * C) / 2
    return retorno

def calculocirculo(C):
    retorno = pi * C ** 2
    return retorno

def calculotrapezio(A,B,C):
    retorno = ((A + B) * C) / 2
    return retorno

def calculoquadrado(B):
    retorno = B ** 2
    return retorno

def calculoretangulo(A,B):
    retorno = A * B
    return retorno

# Chamando funções 
triangulo = calculotriangulo(A,C)
circulo = calculocirculo(C)
trapezio = calculotrapezio(A,B,C)
quadrado = calculoquadrado(B)
retangulo = calculoretangulo(A,B)

# Exibe os resultados com 3 casas decimais
print(f"TRIANGULO: {triangulo:.3f}")
print(f"CIRCULO: {circulo:.3f}")
print(f"TRAPEZIO: {trapezio:.3f}")
print(f"QUADRADO: {quadrado:.3f}")
print(f"RETANGULO: {retangulo:.3f}")