class ConsumoMedio:
    # Parâmetros para cálculo 
    def __init__(self, distancia: int, litros: float):
        self.distancia = distancia
        self.litros = litros
    
    # Calculo médio de consumo por km rodado 
    def consumokm(self):
        return ( self.distancia / self.litros ) 
    
    # Imprimindo retorno    
    def impressao(self):
        print(f'{self.consumokm():.3f} km/l')

# ===== Saída Esperada =====
if __name__ == '__main__':
    # Entrada de valores 
    distancia = int(input())
    litros = float(input())

    # Cria o objeto e executa a função de consumo 
    consumo = ConsumoMedio(distancia,litros)
    consumo.impressao()
