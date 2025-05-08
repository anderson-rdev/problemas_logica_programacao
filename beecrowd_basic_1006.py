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

