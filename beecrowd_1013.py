# BEE 1013 - O Maior
class MaiorAB:
    def __init__(self, A, B, C=None):
        self.A = A
        self.B = B
        self.C = C

    # Calcula o maior entre dois números (A e B)
    def maiorab(self):
        return (self.A + self.B + abs(self.A - self.B)) / 2.0

    # Calcula o maior entre três números (A, B, C)
    def maiorabc(self):
        maior_ab = self.maiorab()
        return (maior_ab + self.C + abs(maior_ab - self.C)) / 2.0

    # Imprime o resultado
    def exibir_resultados(self):
        print(f"{int(self.maiorabc())} eh o maior")


# ===== Programa Principal =====
if __name__ == "__main__":
    A, B, C = map(int, input().split())
    calc = MaiorAB(A, B, C)
    calc.exibir_resultados()
