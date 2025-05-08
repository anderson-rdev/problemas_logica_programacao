# Cálculo da Média Ponderada de Notas
# Este programa lê três notas (variáveis `A`, `B` e `C`) de um aluno e calcula sua **média ponderada**, considerando pesos diferentes para cada nota. A nota `A` tem peso **2**, `B` tem peso **3** e `C` tem peso **5**.

## 💡 Regras
# - Cada nota é um número real (double) com **uma casa decimal**.
# - As notas estão no intervalo de **0.0 a 10.0**.
# - A média deve ser impressa com **exatamente uma casa decimal**, seguindo o formato abaixo.

## 📥 Entrada
# O programa deve ler **três valores de ponto flutuante (double)**, representando as notas `A`, `B` e `C`.

# Exemplo de entrada: 5.0, 6.0, 7.0
# Exemplo de Saída: MEDIA = 6.3

#Criando função 
def calculando_media(a,b,c):
    # Calculano notas com aplicação do peso 
    resultado = ((a * 2) + (b * 3) + (c * 5)) / 10
    return resultado

# Leitura de Dados 
a = float(input(''))
b = float(input(''))
c = float(input(''))

#Chamando função 
result = calculando_media(a,b,c)

# Exibindo resultado
print(f'MEDIA = {result:.1f}')

