class Rentangulo():
    def __init__(self):
        self.largura = int(input("Digite a largura: "))
        self.altura = int(input("Digite a altura: "))

    def calcular(self):
        self.resultado = (self.largura * self.altura)
        print(self.resultado)

rentangulo = Rentangulo()
rentangulo.calcular()