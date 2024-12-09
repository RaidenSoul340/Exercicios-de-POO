class Carro():
    def __init__(self):
        self.marca = input("Digite a marca do carro: ")
        self.modelo = input("Digite o modelo do carro: ")
        self.ano = int(input("Digite o ano do carro: "))

    def descricao(self):
        print(f"O carro que você comprou é da marca {self.marca}, o modelo é {self.modelo}, é do ano {self.ano}")

carro = Carro()
carro.descricao()

'''
Trazendo as informações da Class Carro, utilizando a função descriçao.
'''