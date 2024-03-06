# Desafio 1 Python - Conta Bancária

menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = int(input(menu))

    if opcao == 1:
        valor = float(input('Informe o valor do depósito: '))

        if valor > 0:
            saldo += valor
            extrato += f'Depósito: R$ {valor: .2f}\n'

        else:
            print('Operação falhou! O valor informado é inválido.')

    elif opcao == 2:
        valor = float(input('Informe o valor do saque: '))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite
        
        excedeu_saques = numero_saques >=LIMITE_SAQUES

        if excedeu_saldo:
            print('Operação falhou! Saldo insuficiente para o levantamento indicado')

        elif excedeu_limite:
            print('Operação falhou! O valor do levantamento excede o limite diário')

        elif excedeu_saques:
            print('Operação falhou! Númeor máximo de levantamentos excedido.')

        elif valor > 0:
            saldo -= valor
            extrato = f'Levantamento: R$ {valor: .2f}\n'
            numero_saques += 1

        else:
            print('Operação falhou! O valor informado é inválido.')

    elif opcao == 3:
        print('\n================== EXTRATO ==================')
        print('Não foram realizadas movimentações.' if not extrato else extrato)
        print(f'\nSaldo: R$ {saldo: .2f}')
        print('===============================================')

    elif opcao == 4:
        print('Operação finalizada!')
        break

    else:
        print('Opção inválida. Por favor, digite uma entrada válida!')