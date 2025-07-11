# Leia 3 valores de ponto flutuante A, B e C e ordene-os em ordem decrescente,
#  de modo que o lado A representa o maior dos 3 lados. A seguir, determine o 
# tipo de triângulo que estes três lados formam, com base nos seguintes casos, 
# sempre escrevendo uma mensagem adequada:

# se A ≥ B+C, apresente a mensagem: NAO FORMA TRIANGULO
# se A2 = B2 + C2, apresente a mensagem: TRIANGULO RETANGULO
# se A2 > B2 + C2, apresente a mensagem: TRIANGULO OBTUSANGULO
# se A2 < B2 + C2, apresente a mensagem: TRIANGULO ACUTANGULO
# se os três lados forem iguais, apresente a mensagem: TRIANGULO EQUILATERO
# se apenas dois dos lados forem iguais, apresente a mensagem: TRIANGULO ISOSCELES
# Entrada
# A entrada contem três valores de ponto flutuante de dupla precisão A (0 < A) , B (0 < B) e C (0 < C).

# Saída
# Imprima todas as classificações do triângulo especificado na entrada.

# ## 🧪 Testes Recomendados

# | Entrada        | Saída Esperada                                 |
# | -------------- | ---------------------------------------------- |
# | `6.0 8.0 10.0` | TRIANGULO RETANGULO                            |
# | `6.0 6.0 6.0`  | TRIANGULO ACUTANGULO      TRIANGULO EQUILATERO |
# | `6.0 6.0 10.0` | TRIANGULO OBTUSANGULO      TRIANGULO ISOSCELES |
# | `5.0 7.0 2.0`  | NAO FORMA TRIANGULO                            |

def ler_dados():
  try: 
    # Entrada de dados
    valores = list(map(float, input().split()))
    if len(valores) != 3:
        print("Deve ser inserido exatamente três números.")
        return None
    return valores
  
  except ValueError:
    print("Erro: Entrada inválida. Certifique-se de inserir três números de ponto flutuante.")
    return None

def classificar_triangulo(valores):
    if valores is None:
        return
    
    # Desempacotando os valores
    A, B, C = valores
    
    # Ordena em Ordem decrescente
    valores.sort(reverse=True) 
    A, B, C = valores 

    # Verifica se forma triângulo 
    if A >= B + C: 
        print("NAO FORMA TRIANGULO")
        return
    
    # Verifica tipo quanto aos ângulos
    if A**2 == B**2 + C**2: 
        print("TRIANGULO RETANGULO")      
    elif A**2 > B**2 + C**2: 
        print("TRIANGULO OBTUSANGULO")          
    else:   
        print("TRIANGULO ACUTANGULO")  
    
    # Verifica se exite lados três ou dois lados iguais
    if A == B == C: 
        print("TRIANGULO EQUILATERO")    
    elif A == B or B == C or A == C: 
        print("TRIANGULO ISOSCELES")

# Função Principal
def main():
    valores = ler_dados()
    classificar_triangulo(valores)

if __name__ == "__main__":
    main()
