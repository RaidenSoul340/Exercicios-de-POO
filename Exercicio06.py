class ContaBancaria():

    def __init__(self):
        self.titulo = input("Digite o nome do titlular: ")
        self.saldo = float(input("Digite o seu saldo: "))

    def depositar(self):
        while True:
            self.pergunta = input("Você deseja depositar?(sim/nao): ")
            
            if self.pergunta == "sim":
                self.deposito = float(input("Digite o valor de deposito: "))
                self.valorTotal = (self.saldo + self.deposito)
                print(self.valorTotal)

            elif self.pergunta == "nao":
                print("encerrando operação!...")
                break
            
            else:
                print("por favor apenas 'sim' ou 'nao'...")

    def sacar(self):
            self.pergunta = input("Você deseja sacar?(sim/nao): ")
            if self.pergunta == "sim":
                    self.saque = float(input("Quanto você deseja sacar? "))
                    self.TotalSaque = (self.saque - self.saldo)

                    if self.TotalSaque >= 1:
                        print(self.TotalSaque)

                    elif self.TotalSaque <= 0:
                        print("Seu saldo não pode ser negativo saque menos por favot")

                    else:
                        print("valor desconhecido tente novamente!")

caixa = ContaBancaria()
while True:
    escolha = input("O que deseja realizar depositar, sacar, encerrar?: ")

    if escolha == "depositar":
        caixa.depositar()

    elif escolha == "sacar":
        caixa.sacar()

    elif escolha == "encerrar":
        break

    else:
        print("Valor desconhecido tente novamente!")