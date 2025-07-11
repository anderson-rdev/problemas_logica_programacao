# Leia quatro números (N1, N2, N3, N4), cada um deles com uma casa decimal, correspondente às 
# quatro notas de um aluno. Calcule a média com pesos 2, 3, 4 e 1, respectivamente, para cada
# uma destas notas e mostre esta média acompanhada pela mensagem "Media: ". 

# Etapa 1° - Se esta média for  maior ou igual a 7.0, imprima a mensagem "Aluno aprovado.".  
# Etapa 2° - Se a média calculada for inferior a 5.0, imprima a mensagem "Aluno reprovado.". 
# Etapa 3° - Se a média calculada for um valor entre 5.0 e 6.9, inclusive estas, o programa deve imprimir a mensagem "Aluno em exame."

# No caso do aluno estar em exame, leia um valor correspondente à nota do exame obtida pelo aluno. 
# Imprima então a mensagem "Nota do exame: " acompanhada pela nota digitada. Recalcule a média 
# (some a pontuação do exame com a média anteriormente calculada e divida por 2). e imprima a
#  mensagem "Aluno aprovado." (caso a média final seja 5.0 ou mais ) ou "Aluno reprovado.", 
# (caso a média tenha ficado 4.9 ou menos). Para estes dois casos (aprovado ou reprovado após ter pego exame) 
# apresente na última linha uma mensagem "Media final: " seguido da média final para esse aluno.

# Entrada
# A entrada contém quatro números de ponto flutuante correspendentes as notas dos alunos.

# Saída
# Todas as respostas devem ser apresentadas com uma casa decimal.
#  As mensagens devem ser impressas conforme a descrição do problema.
#  Não esqueça de imprimir o enter após o final de cada linha, caso contrário obterá "Presentation Error".

# Criando Função
def calcular_media(N1 ,N2 ,N3, N4):
    # Calculando média com peso
    return ( ( ( float(N1) * 2) + ( float(N2) * 3 ) + ( float(N3) * 4 ) + (float(N4) * 1 )) / 10)

try:
    # Entrada de dados
    notas = list(map(float, input().split()))

    if len(notas) != 4:
        print("Deve ser inserido exatamente quatro números.")
    else:
        # Desempacotando as notas
        N1 ,N2 ,N3, N4 = notas
        # Chamando função
        media = calcular_media(N1 ,N2 ,N3, N4)
        print(f'Media: {media:.1f}')
        # Definindo status de aprovação do aluno 
        if media >= 7.0: 
            print("Aluno aprovado.")
        elif media < 5.0:     
            print("Aluno reprovado.")
        else:
            print("Aluno em exame.")
            exame = float(input("Digite a nota do exame: "))
            print(f"Nota do exame: {exame:.1f}")
            
            media_final = (media + exame) / 2
            if media_final >= 5.0:
                print("Aluno aprovado.")
            else:
                print("Aluno reprovado.")
            print(f"Media final: {media_final:.1f}")
except ValueError:
    print("Erro: Entrada inválida. Certifique-se de inserir quatro números de ponto flutuante.")
    

