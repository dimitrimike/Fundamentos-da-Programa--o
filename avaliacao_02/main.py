from paciente import Paciente
from paciente_particular import PacienteParticular
from paciente_convenio import PacenteConvenio

def main():
    # Criando um paciente particular
    paciente_particular = PacienteParticular(
        nome="João Silva",
        data_nascimento="01/01/1990",
        cpf="12345678900",
        telefone="99999-9999",
        tipo_sanguineo="O+",
        numero_prontuario="001",
        forma_pagamento="Cartão de Crédito",
        desconto_fidelidade="Sim"
    )

    # Registrando um atendimento para o paciente particular
    print(paciente_particular.registrar_atendimento("Consulta", 150.0))
    print(paciente_particular.calcular_valor_final(taxa_urgencia=50.0))

    # Criando um paciente com convênio
    paciente_convenio = PacenteConvenio(
        nome="Maria Souza",
        data_nascimento="02/02/1985",
        cpf="98765432100",
        telefone="88888-8888",
        tipo_sanguineo="A-",
        numero_prontuario="002",
        nome_convenio="Saúde Plus",
        numero_carteirinha="123456"
    )

    # Registrando um atendimento para o paciente com convênio
    print(paciente_convenio.registrar_atendimento("Exame", 200.0))
    print(paciente_convenio.registrar_autorizacao("Autorizado", glosa=0.0, pagamento_convenio=True))