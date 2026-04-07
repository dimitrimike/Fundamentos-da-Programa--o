print("Sistema de Empréstimo Bancário")

# Entrada dos dados
idade = int(input("Digite a idade: "))
salario = float(input("Digite o salário do cliente: "))
tempo_trabalhado = int(input("Digite o tempo trabalhado (em anos) do cliente: "))

# Estruturas condicionais
if idade < 18:
    print("Empréstimo negado. Cliente menor de idade.")
elif salario >= 5000:
    print("Empréstimo aprovado automaticamente.")
elif idade >= 18 and salario >= 2000 and tempo_trabalhado >= 2:
    print("Empréstimo aprovado.")
else:
    print("Empréstimo negado.")