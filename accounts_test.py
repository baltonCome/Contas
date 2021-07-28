import random
import time

from accounts import account

bank_open = True

contas = []

while bank_open:
    choice = int(input('[1]Registar\n[2]Depositos\n[3]Levantamentos\n[4]Extrato\n[5]Mostrar Contas\n[6]Remover Conta\n[7]Transferir\n[0]Sair\n>>>>>'))
    if choice == 1:
        acc = random.randint(1000, 9999)
        save_account = account(input('Nome: '), acc, float(input('Saldo Inicial: ')))
        contas.append(save_account)
        print(f"Conta Registada, Numero da Conta: {acc}")
        time.sleep(2)
    elif choice == 2:
        conta = int(input('Numero da Conta: '))
        for key, val in enumerate(contas):
            if conta == val.nr_conta:
                contas[key].deposito(float(input('Valor do Deposito: ')))
                print('Deposito efectuado')
                time.sleep(2)
                break
            else:
                print('Operacao Nao sucedida')
                time.sleep(2)
    elif choice == 3:
        conta = int(input('Numero da Conta: '))
        for key, val in enumerate(contas):
            if conta == val.nr_conta:
                contas[key].levanta(float(input('Valor do Levantamento: ')))
                time.sleep(2)
                break
            else:
                print('Operacao Nao sucedida')
                time.sleep(2)
    elif choice == 4:
        conta = float(input('Numero da conta: '))
        for key, val in enumerate(contas):
            if conta == val.nr_conta:
                contas[key].extrato(conta)
                time.sleep(2)
    elif choice == 5:
        for account in contas:
            account.exibe()
    elif choice == 6:
        conta = int(input('Numero Da conta: '))
        found = False
        for key, val in enumerate(contas):
            if conta == val.nr_conta:
                del contas[key]
                print('Conta Removida')
                time.sleep(3)
            else:
                print('Operacao sem Sucesso')
    elif choice == 7:
        found = False
        exist = False
        origem = int(input('Conta de Origem: '))
        for key_source, val in enumerate(contas):
            if origem == val.nr_conta:
                found = True
                break
        destino = int(input('Conta de Destino: '))
        for key_destination, val in enumerate(contas):
            if destino == val.nr_conta:
                exist = True
                break
        if found and exist:
            contas[key_source].transfere(contas[key_destination], float(input("Valor a Depositar: ")))
        else:
            print('Operacao sem Sucesso')
    elif choice == 0:
        bank_open = False
    else:
        print('Escolha Invalida')
        time.sleep(1)
