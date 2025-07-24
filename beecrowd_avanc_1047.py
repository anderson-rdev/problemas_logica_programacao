# Leia a hora inicial, minuto inicial, hora final e minuto final de um jogo. A seguir calcule a duração do jogo.
# Obs: O jogo tem duração mínima de um (1) minuto e duração máxima de 24 horas.

# Entrada
# Quatro números inteiros representando a hora de início e fim do jogo.

# Saída
# Mostre a seguinte mensagem: “O JOGO DUROU XXX HORA(S) E YYY MINUTO(S)” .

# Definindo a função principal 
def calcular_duracao_jogo(hora_inicial, minuto_inicial, hora_final, minuto_final):
    # Converte horários para minutos desde a meia-noite
    inicio_total_min = hora_inicial * 60 + minuto_inicial
    fim_total_min = hora_final * 60 + minuto_final

    # Se os horários forem iguais, o jogo durou 24 horas
    if inicio_total_min == fim_total_min:
        duracao_minutos = 24 * 60
    else:
        # Cálcula modular para lidar com passagem da meia-noite
        duracao_minutos = (fim_total_min - inicio_total_min) % (24 * 60)

    # Converte a duração total de minutos para horas e minutos
    horas = duracao_minutos // 60
    minutos = duracao_minutos % 60

    # Retorno formatado da duração do jogo
    return f'O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)'

# Entrada dos dados
entrada = input().split()
hora_inicial = int(entrada[0])
minuto_inicial = int(entrada[1])
hora_final = int(entrada[2])
minuto_final = int(entrada[3])

# Chamada da função e impressão do resultado
resultado = calcular_duracao_jogo(hora_inicial, minuto_inicial, hora_final, minuto_final)
print(resultado)