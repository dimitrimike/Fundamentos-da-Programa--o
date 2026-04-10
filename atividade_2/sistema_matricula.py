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