saldo = 1000.00
historico = [] # Lista Vazia

print(f'🏧 --- Bem-vindo ao Caixa Eletrônico ---')

while True: # Imprime pelo menos o while uma vez
    print(f''' --- Menu Principal ---
            [1] - Depositar
            [2] - Sacar
            [3] - Ver Saldo
            [4] - Ver Histórico
            [5] - Sair
    ''')
    opcao = input('➡️ Escolha uma opção:')

    # Lógica para a opção de Depósito
    if opcao == '1':
        valor_deposito = float(input('➡️ Digite o valor para Depósito: R$'))
        if valor_deposito > 0:
            saldo += valor_deposito # saldo + valor_deposito
            registro = f'Depósito: + R${valor_deposito:.2f}'
            historico.append(registro) # append() adiciona algo a lista
            print('🆗 Depósito realizado com sucesso.')
        else:
            print('❌ Valor inválido. O Depósito deve ser um número positivo.')
    elif opcao == '2':
        valor_saque = float(input('➡️ Digite o valor para Depósito: R$'))
        if valor_saque <= 0:
            print('❌ Valor inválido. O saque deve ser um número positivo.')
        elif valor_saque > saldo:
            print('❌ Saldo insuficiente para realizar este saque.')
        else:
            saldo -= valor_saque # saldo = saldo - valor_saque
            registro = f'Saque: - R${valor_saque:.2f}'
            historico.append(registro)
            print('🆗 Saque realizado com sucesso! Retire o seu dinheiro.')
    elif opcao == '3':
        print(f'💰 Seu saldo atual é: {saldo:.2f}')
    elif opcao == '4':
        print('🧾 --- Histórico de Transações ---')
        if not historico: # Verifica se histórico está vazia, pois toda variável/estrutura vazia é True po padrão.
            print('❌ Nenhuma transação foi realizada ainda.')
        else:
            for transacao in historico: 
                print(transacao)
    elif opcao == '5':
        print('😊 Obrigado poe utilizar nosso Caixa Eletrônico. Finalizando ...')
        break # Encera o laço while
    else:
        print('❌ Opção inválida. Por favor, escolha uma das opções do menu')
