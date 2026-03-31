# Sistema de Empréstimo Bancário

# Objetivo: Criar um programa para analizar se um cliente pode receber um empréstimo.

# Regras: Idade >= 18 / Salário >= 2000 / Tempo de trabalho >= 2 anos

# Regras Especiais: Idade < 18 Emprétimo NEGAÇÃO AUTOMÁTICA / Salário >= 5000 APROVAÇÃO AUTOMÁTICA

# Informações: 

idade_cliente = input ("Informe a idade do cliente:")
salário_cliente = input ("Informe o salário do cliente em reais:")
tempo_trabalho = input ("Informe o tempo de trabalho do cliente em anos:")

# Código:

if int(idade_cliente) >= 18 and int(salário_cliente) >= 2000 and int(tempo_trabalho) >= 2:
    print(f"Empréstimo Aprovado. Cliente tem {idade_cliente} anos, salário de {salário_cliente} reais e {tempo_trabalho} anos de trabalho.")
elif int(idade_cliente) < 18:
    print("Empréstimo negado, menor de idade.")
elif int(salário_cliente) >= 5000:
    print(f"Empréstimo Aprovado! VIP! Cliente tem salário de {salário_cliente} reais!")
else:
    print("Empréstimo negado. CLiente não atende todos os requisitos mínimos")