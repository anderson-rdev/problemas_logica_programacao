## 📘 Descrição do Problema
# Leia dois valores inteiros, armazenando-os nas variáveis **A** e **B**. Em seguida, calcule a soma desses dois valores e armazene o resultado na variável **SOMA**. Por fim, exiba o valor da variável **SOMA** no formato especificado.

## 📥 Entrada
# O programa deve ler dois valores inteiros, um por linha.
# Esses valores representam os números **A** e **B** que serão somados.

## 📤 Saída
# O programa deve imprimir a mensagem:
# SOMA = X

# Onde `X` é o valor da soma de **A** e **B**.
# A palavra **SOMA** deve estar em letras maiúsculas, e deve haver **um espaço em branco antes e depois do sinal de igual (`=`)**.
# ⚠️ **Importante:** Não se esqueça de adicionar uma **quebra de linha (`\n`)** ao final da saída. A ausência disso causará um erro do tipo **"Presentation Error"** na plataforma.

## ✅ Exemplos
# | Entrada   | Saída      |
# | --------- | ---------- |
# | 30<br>10  | SOMA = 40  |
# | -30<br>10 | SOMA = -20 |
# | 0<br>0    | SOMA = 0   |

# Criando Função
def adding_new(a,b):
    # Calculo(Adição)
    result = (a+b)
    return result

#Leitura de Dados
a = int(input())
b = int(input())

# Chamada da função para soma dos valores
adding = adding_new(a,b)

# Imprimindo o resultado
print(f'SOMA = {adding}')