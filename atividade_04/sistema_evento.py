print("Sistema de controle de entrada para o evento")

# Entrada de dados
nome = input("Digite o nome da pessoa: ")
idade = int(input("Digite a idade da pessoa: "))
convite = input("Digite se a pessoa tem convite, Sim ou Não: ")

# Estruturas condicionais
while True:
    if idade >= 16 and convite == "Sim":
        print("Entrada permitida")
    elif idade < 16 or convite == "Não":
        print("Entrada negada")
    if input("Encerrar"):
        break