class Livro():
    def __init__(self):
        self.titulo = input("Digite o titulo do livro: ")
        self.autor = input("Digite o nome do Autor: ")
        self.numero_paginas = int(input("Digite o número de paginas: "))
        
    def ler_Pagina(self):
        self.pagina = int(input("Digite a pagina atual: "))
        print(f"Você esta lendo a página {self.pagina} do livro")

livro = Livro()
livro.ler_Pagina()
