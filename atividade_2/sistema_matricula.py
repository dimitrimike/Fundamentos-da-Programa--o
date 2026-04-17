print("Sistema de Matrícula em Curso")

# Entrada dos Dados
idade = int(input ("Informe a idade: "))
nota_prova = float(input ("Informe a nota na prova: "))
frequencia_escolar = float(input ("Informe a frequência escolar em %: "))


# Estruturas condicionais
if idade >= 18 and nota_prova >= 6 and frequencia_escolar >= 75:
    print("Matricula aprovada.")
elif idade < 18:
    print("Matricula negada. Aluno menor de idade.")
elif nota_prova >= 9:
    print("Matricula aprovada automaticamente")
else:
    print("Matricula negada.")


    print("Sistema de controle de entrada para o evento")

# Entrada de dados
nome = input("Digite o nome da pessoa: ")
idade = int(input("Digite a idade da pessoa: "))
convite = input("Digite se a pessoa tem convite, Sim ou Não: ")


# Estruturas condicionais
if idade >= 16 and convite == "Sim":
    print("Entrada permitida")
elif idade < 16 or convite == "Não":
    print("Entrada negada")
while True:
    print("Sistema de controle de entrada para o evento")
    if input("Encerrar"):
        break