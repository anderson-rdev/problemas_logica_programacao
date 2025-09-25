# ******************************************************************************************
# * Faça um programa que calcule e mostre o volume de uma esfera, sendo fornecido o valor  *
# * de seu raio (R). A fórmula para calcular o volume é:                                   *
# *                                 (4/3) * pi * R³                                        *
# *                                                                                        *
# * Considere (atribua) para pi o valor: 3.14159                                           *
# *                                                                                        *
# * Dica: Ao utilizar a fórmula, procure usar (4/3.0) ou (4.0/3), pois algumas linguagens  *
# * (dentre elas o C++), assumem que o resultado da divisão entre dois inteiros é outro    *
# * inteiro (ignorando as casas decimais).                                                 *
# *                                                                                        *
# * Entrada:                                                                               *
# * - O arquivo de entrada contém um valor de ponto flutuante (dupla precisão),            *
# *   correspondente ao raio da esfera.                                                    *
# *                                                                                        *
# * Saída:                                                                                 *
# * - A saída deverá ser uma mensagem "VOLUME", conforme o exemplo abaixo,                 *
# *   com um espaço antes e um espaço depois da igualdade.                                 *
# * - O valor deverá ser apresentado com 3 casas decimais.                                 *
# ******************************************************************************************
# Importando biblioteca 
from math import pow 

# Entrada de dados 
raio = int(input("Informe o raio:"))

# Função para calcular da volume de uma esfera
def calculando_volume(raio):
    calculo = (4/3.0) * 3.14159 * (pow(raio,3))
    return calculo
    
# Aplicando função 
volume = calculando_volume(raio)   

# Imprimindo resultado
print(f'Resultado: {volume:.3f}') 