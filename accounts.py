import time

class account:

    def __init__(self, nome, nr_conta, saldo):
        self.nome = nome
        self.nr_conta = nr_conta
        self.saldo = saldo

    def deposito(self, valor):
        self.saldo += valor

    def levanta(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print("Operacao falhada")

    def extrato(self, numero):
        print(f"Saldo da Conta: {self.saldo}")
        time.sleep(3)

    def exibe(self):
        print(f"Numero da Conta: {self.nr_conta}")
        print(f"Titular: {self.nome}")
        print(f"Saldo da Conta: {self.saldo}")
        print(f"--------------------------------")
        time.sleep(3)

    def transfere(self, destino, valor):
        self.levanta(valor)
        destino.deposito(valor)