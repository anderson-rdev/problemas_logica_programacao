# Problema: Cálculo da Área de uma Circunferência

# Descrição
# A fórmula para calcular a área de uma circunferência é:

# ```
# área = π × raio²
# ```

# Para este problema, considere que o valor de c é 3.14159.

# Você deve:

# - Ler um valor de ponto flutuante de dupla precisão (double), representando o raio.
# - Calcular a área utilizando a fórmula acima.
# - Exibir a saída no formato especificado, com 4 casas decimais após o ponto e uma quebra de linha ao final.

#  Entrada
# - Um valor de ponto flutuante do tipo `double`, representando o raio da circunferência.

#  Saída
# - Exibir a mensagem no formato:  
#   ```
#   A=área_calculada
#   ```
#   - A área deve ser impressa com 4 casas decimais.
#   - Não esquecer a quebra de linha ao final para evitar erro de apresentação ("Presentation Error").

# ---

#  Exemplos
# ----------------------------
# | Entrada   | Saída        |
# |-----------|--------------|
# | 2.00      | A=12.5664    |
# | 100.64    | A=31819.3103 |
# | 150.00    | A=70685.7750 |
# ----------------------------

# Código Abaixo:  
def calculando_raio(raio):
    # Calcula a área de uma circunferência com base no raio
    return 3.14159 * (raio ** 2)

# Leitura de Dados
raio = float(input())

# Chamada da função para obter a área
area = calculando_raio(raio)

# Saída formatada com 4 casas decimais
print(f'A={area:.4f}')