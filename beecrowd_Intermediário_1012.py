# BEE 1012 - Área
class CalculandoraAreas:
    def __init__(self, A: float, B: float, C: float):
        self.A = A
        self.B = B
        self.C = C
        self.pi = 3.14159

# Calcula as áreas
    def triangulo(self):
        return (self.A * self.C) / 2

    def circulo(self):
        return self.pi * self.C ** 2
        
    def trapezio(self):
        return ((self.A + self.B) * self.C) / 2
         
    def quadrado(self):
        return self.B ** 2

    def retangulo(self):
        return  self.A * self.B
    
# Imprindo resultado    
    def exibir_resultados(self):
        print(f"TRIANGULO: {self.triangulo():.3f}")
        print(f"CIRCULO: {self.circulo():.3f}")
        print(f"TRAPEZIO: {self.trapezio():.3f}")
        print(f"QUADRADO: {self.quadrado():.3f}")
        print(f"RETANGULO: {self.retangulo():.3f}")    

# ===== Programa Principal =====
if __name__ == "__main__":
    # Entrada dos valores
    A, B, C = map(float, input().split())

    # Cria o objeto e executa os cálculos
    calc = CalculandoraAreas(A, B, C)
    calc.exibir_resultados()