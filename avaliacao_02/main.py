from paciente_particular import PacienteParticular
from paciente_convenio import PacienteConvenio

# Rode o código 3 vezes
# Na primeira vez dará erro e o código informará como corrigir, corrija e rode novamente
# Na segunda vez o dará erro novamente e o código informará como corrigir, corrija e rode de novo
# Na terceira vez o código rodará sem falhas

def main():
    # Pacientes particular
    paciente_particular1 = PacienteParticular(nome="João Silva", data_nascimento="01/01/1990", cpf="123.456.789-00", telefone="(11) 98765-4321", tipo_sanguineo="O+", numero_prontuario="12345", forma_pagamento="Cartão de Crédito", desconto_fidelidade="sim")
    paciente_particular2 = PacienteParticular(nome="Ana Oliveira", data_nascimento="10/10/1985", cpf="987.654.321-00", telefone="(21) 91234-5678", tipo_sanguineo="A-", numero_prontuario="67890", forma_pagamento="Dinheiro", desconto_fidelidade="não")
    paciente_particular3 = PacienteParticular(nome="Pedro Santos", data_nascimento="20/08/1975", cpf="456.789.123-00", telefone="(31) 99876-5432", tipo_sanguineo="B+", numero_prontuario="54321", forma_pagamento="Boleto Bancário", desconto_fidelidade="positivo")

    print("     Pacientes Particulares: ")
    print(paciente_particular1.registrar_atendimento("Cirurgia Urgente", 800.0))
    print(paciente_particular1.exibir_informacoes())
    print(paciente_particular1.exibir_informacoes(detalhado=True))
    print(paciente_particular1.exibir_informacoes_particular())
    print(paciente_particular1.calcular_valor_final())
    print("\n ---------------------------")

    print(paciente_particular2.registrar_atendimento("Exame", 200.0))
    print(paciente_particular2.exibir_informacoes_particular())
    print(paciente_particular2.calcular_valor_final())
    print("\n ---------------------------")

    print(paciente_particular3.registrar_atendimento("Raio X", 180.0))
    print(paciente_particular3.exibir_informacoes_particular())
    print(paciente_particular3.calcular_valor_final())
    print("\n ---------------------------")



    # Pacientes com convênio
    paciente_convenio1 = PacienteConvenio(nome="Maria Souza", data_nascimento="15/05/1985", cpf="987.654.321-00", telefone="(21) 91234-5678", tipo_sanguineo="A-", numero_prontuario="67890", nome_convenio="Saúde Total", numero_carteirinha="ST123456")
    paciente_convenio2 = PacienteConvenio(nome="Carlos Lima", data_nascimento="20/08/1975", cpf="456.789.123-00", telefone="(31) 99876-5432", tipo_sanguineo="B+", numero_prontuario="54321", nome_convenio="Bem Estar Saúde", numero_carteirinha="BE987654")
    paciente_convenio3 = PacienteConvenio(nome="Fernanda Costa", data_nascimento="05/03/1992", cpf="321.654.987-00", telefone="(41) 98765-4321", tipo_sanguineo="AB-", numero_prontuario="98765", nome_convenio="Vida Plena", numero_carteirinha="VP654321")
    
    print("\n     Pacientes Convenios: ")
    print(paciente_convenio1.registrar_atendimento("Cirurgia Urgente", 900.0))
    print(paciente_convenio1.exibir_informacoes_convenio())
    print(paciente_convenio1.registrar_autorizacao("confirmado"))
    print("\n ---------------------------")

    print(paciente_convenio2.registrar_atendimento("Exame", 300.0))
    print(paciente_convenio2.exibir_informacoes_convenio())
    print(paciente_convenio2.registrar_autorizacao("negado"))
    print("\n ---------------------------")

    print(paciente_convenio3.registrar_atendimento("Raio X", 280.0))
    print(paciente_convenio3.exibir_informacoes_convenio())
    print(paciente_convenio3.registrar_autorizacao("sim"))
    print("\n ---------------------------")

   


if __name__ == "__main__":
    main()
