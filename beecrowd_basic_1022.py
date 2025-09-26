# ****************************************************************************
# Escreva um programa que leia três valores com ponto flutuante 
# de dupla precisão: A, B e C. Em seguida, calcule e mostre:
# 
# a) a área do triângulo retângulo que tem A por base e C por altura.
# b) a área do círculo de raio C. (pi = 3.14159)
# c) a área do trapézio que tem A e B por bases e C por altura.
# d) a área do quadrado que tem lado B.
# e) a área do retângulo que tem lados A e B.
# 
# Entrada
# O arquivo de entrada contém três valores com um dígito após o ponto decimal.
# 
# Saída
# O arquivo de saída deverá conter 5 linhas de dados. Cada linha corresponde 
# a uma das áreas descritas acima, sempre com mensagem correspondente e um espaço 
# entre os dois pontos e o valor. O valor calculado deve ser apresentado com 
# 3 dígitos após o ponto decimal.
# **********************************************************************************

# Entrada de dados 
a, b, c = [float(x) for x in input()]

# ** Funções para calcular a área **  

# A área do triângulo retângulo que tem A por base e C por altura.
def AreaRetangulo(a, c):
    calculoretangulo = ((a * c) / 2)
    return calculoretangulo

# A área do círculo de raio C. (pi = 3.14159)
def AreaCirculo(c):
    calculocirculo = (3.14159 * ( c * c))
    return calculocirculo

# c) a área do trapézio que tem A e B por bases e C por altura.
def AreaTrapezio (a, b, c):
    calculotrapezio = ((( a +b ) * c) / 2)
    return calculotrapezio

# d) a área do quadrado que tem lado B.
def LadoB(b):
    ladob = (b * b)
    return ladob

# e) A área do retângulo que tem lados A e B.
def LadoAB(a, b):
    ladoab = (a * b)
    return ladoab

# Aplicando funções
calculoretangulo = AreaRetangulo(a,c)
areacirculo = AreaCirculo(c)
calculotrapezio = AreaTrapezio(a,b,c)
Ladob = LadoB(b)
ladoab = LadoAB(a,b)

# Imprimindo resultado 
print(f'TRIANGULO: {calculoretangulo:.3f}')
print(f'CIRCULO: {areacirculo:.3f}')
print(f'TRAPEZIO: {calculotrapezio:.3f}')
print(f'QUADRADO: {Ladob:.3f}')
print(f'RETANGULO: {calculotrapezio:.3f}')
