# Classe Filha - Subclass

from paciente import Paciente

class PacenteConvenio(Paciente):
    def __init__(self, nome, data_nascimento, cpf, telefone, tipo_sanguineo, numero_prontuario, nome_convenio, numero_carteirinha):
        super().__init__(nome, data_nascimento, cpf, telefone, tipo_sanguineo, numero_prontuario)
        self.nome_convenio = nome_convenio
        self.numero_carteirinha = numero_carteirinha

    def exibir_informacoes(self):
        informacoes_paciente = super().exibir_informacoes()
        return f''' {informacoes_paciente}
    Nome do convenio: {self.nome_convenio}
    Número da carteirinha: {self.numero_carteirinha}

        '''