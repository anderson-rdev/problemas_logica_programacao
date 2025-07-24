# Leia a hora inicial, minuto inicial, hora final e minuto final de um jogo. A seguir calcule a duração do jogo.

# Obs: O jogo tem duração mínima de um (1) minuto e duração máxima de 24 horas.

# Entrada
# Quatro números inteiros representando a hora de início e fim do jogo.

# Saída
# Mostre a seguinte mensagem: “O JOGO DUROU XXX HORA(S) E YYY MINUTO(S)” .

# Exemplo de Entrada
hora_inicial, minuto_inicial, hora_final, minuto_final = map(int, input().split())

# Exemplo de Saída 
if hora_inicial == hora_final and minuto_inicial == minuto_final:
    print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
elif hora_inicial < hora_final or (hora_inicial == hora_final and minuto_inicial < minuto_final):
    duracao_horas = hora_final - hora_inicial
    duracao_horas += ((minuto_final - minuto_inicial) // 60)
    duracao_horas = duracao_horas % 24
    duracao_minutos = (minuto_final - minuto_inicial) % 60
    print(f'O JOGO DUROU {duracao_horas} HORA(S) E {duracao_minutos} MINUTO(S)')
else:
    duracao_horas = (hora_final + 24) - hora_inicial
    duracao_horas += ((minuto_final - minuto_inicial) // 60)
    duracao_horas = duracao_horas % 24 
    duracao_minutos = (minuto_final - minuto_inicial) % 60
    print(f'O JOGO DUROU {duracao_horas} HORA(S) E {duracao_horas} MINUTO(S)')
