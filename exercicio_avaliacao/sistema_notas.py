print("Sistema de Gerenciamento de Notas de Alunos")

# Boletim da Turma
boletim = []

while True: 
    print(f''' --- Menu Principal ---
          [1] - Cadastrar Aluno
          [2] - Acessar Boletim da Turma
          [3] - Encerrar ''')
    comando = input ('Escolha uma opção:')
    if comando == '1':
        nome_aluno = input('Digite o nome do aluno: ')
        nota_1 = float(input('Digite a primeira nota do aluno: '))
        nota_2 = float(input('Digite a segunda nota do aluno: '))
        nota_3 = float(input('Digite a terceira nota do aluno: '))
        media = (nota_1 + nota_2 + nota_3)/3
        #if nota_1 < 0 or nota_1 > 10:
            print("Nota inválida")
        elif media >= 7:
            print(f'Média{media}: Aprovado')
            situacao = 'Aprovado'
        elif media >= 5 < 7:
            print(f'Média{media}: Recuperação')
            situacao = 'Recuperação'
        elif media < 5:
            print(f'Média{media}: Reprovado')
            situacao = 'Reprovado'
        registro = f'''
        Aluno:{nome_aluno} 
        Notas:{nota_1},{nota_2},{nota_3}
        Média:{media}
        Situação:{situacao}'''
        boletim.append(registro)
    elif comando == '2':
        print('-- Boletim da Turma --')
        if not boletim:
            print('Nenhum aluno cadastrado')
        else:
            for aluno in boletim:
                print(aluno)
    elif comando == '3':
        print('Encerando o sistema')
        break