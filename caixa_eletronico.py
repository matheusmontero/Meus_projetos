print('=' * 20 , 'CAIXA ELETRÔNICO' , '=' * 20 )
saldo = float(input('Diga um saldo para começarmos: '))
print('==' * 30)
print('Saldo inicial de R${:.2f}'.format(saldo))
while True:
    print('1 - Ver saldo | 2 - Depositar | 3 - Fazer saque | 4 - Sair')
    opcao = input('Escolha uma opcao: ')
    if opcao == '1':
        print('Seu saldo é de R${:.2f} '.format(saldo))
    elif opcao == '2':
        valor = float(input('Valor do depósito: R$'))
        if valor > 0:
            saldo += valor
            print('Valor do depósito de R${} realizado.'.format(valor))
        else:
            print('Valor inválido! ')
    elif opcao == '3':
        valor = float(input('Valor do saque: R$'))
        if valor <= saldo:
            saldo -= valor
            print('Saque de R${} realizado.'.format(valor))
        elif valor > saldo:
            print('Saldo insuficiente.')
        else:
            print('Valor invalido.')
    elif opcao == '4':
        print('Encerrando... Obrigado!')
        break
    else:
        print('Opção inválida, tente novamente ')