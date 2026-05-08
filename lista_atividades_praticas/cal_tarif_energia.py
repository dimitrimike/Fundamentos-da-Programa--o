print('Calculadora de Tarifa de Energia')

while True:
    print(f''' --- Menu Principal ---
          [1] - Nova Cobrança
          [2] - Históricos de Tarifas
          [3] - Encerrar
          ''')
    comando = input ('Escolha uma opção: ')

    if comando == '1':
        nome_cliente = input('Digite o nome do cliente: ')
        consumo = float(input('Digite o consumo de energia em kWh: '))
        if consumo <= 100:
            tarifa1 = consumo*0.40
            print(f'Tarifa R$0,40 por kWh: R${tarifa1:.2f}')
        elif consumo > 100 <= 200:
            tarifa2 = (consumo - 100)*0.60
            print(f'Tarifa R$40,00 + R${tarifa2:.2f}: RS{tarifa2+40:.2f}')
        elif consumo > 200:
            tarifa3 = (consumo - 200)*0.90
            print(f'Tarifa R$40,00 + R$60,00 + R${tarifa3:.2f}: R${tarifa3+100:.2f}')

    elif comando == '3':
        break
        