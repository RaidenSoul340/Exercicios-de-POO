class Pessoa():
    def __init__(self):
        self.nome = input("digite seu nome: ")
        self.idade = int(input("digite sua idade: "))
    
    def apresentar(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")

pessoa = Pessoa()
pessoa.apresentar()

'''
trazendo as informações da Classe Pessoa, utilizando a função aprensetar.
'''