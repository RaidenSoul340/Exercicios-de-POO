class Produto():
    def __init__(self):
        self.nome = input("Digite o nome do produto: ")
        self.preco = float(input("Digite o valor do produto: "))
        self.quantidade = int(input("Digite a quantidade de produto: "))

    def atualizar_estoque(self):
        self.atualizar = input("Deseja atualizar o estoque?(sim/nao): ")
        if self.atualizar == "sim":
            self.esc = input("Deseja adicionar ou remover?: ")
            if self.esc == "adicionar":
                self.ValorPositivo = int(input("quantos itens deseja adicionar? "))
                self.total = (self.quantidade + self.ValorPositivo)
                print(f"A quantidade foi atualizada para {self.total}")

            elif self.esc == "remover":
                self.ValorNegativo = int(input("quantos itens deseja remover?: "))
                self.total = (self.quantidade - self.ValorNegativo)
                print(f"A quantidade foi atualizada para {self.total}")

        elif self.atualizar == "nao":
            print("Encerrando operação!...")

produto = Produto()
produto.atualizar_estoque()

