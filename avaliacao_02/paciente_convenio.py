# Classe Filha - Subclass

from paciente import Paciente

class PacenteConvenio(Paciente):
    def __init__(self, nome: str, data_nascimento: str, cpf: str, telefone: str, tipo_sanguineo: str, numero_prontuario: str, nome_convenio: str, numero_carteirinha: str):
        super().__init__(nome, data_nascimento, cpf, telefone, tipo_sanguineo, numero_prontuario)
        self.nome_convenio = nome_convenio
        self.numero_carteirinha = numero_carteirinha

    def exibir_informacoes(self):
        informacoes_paciente = super().exibir_informacoes()
        return f''' {informacoes_paciente}
    Nome do convenio: {self.nome_convenio}
    Número da carteirinha: {self.numero_carteirinha}

        '''
    
    def registrar_autorizacao(self, procedimento: str, glosa: float, pagamento_convenio: bool):
        atendimento = super().registrar_atendimento()
        glosa = self.custo_atendimento
        if procedimento.lower() == 'Autorizado' and pagamento_convenio == True:
            return f''' {atendimento}
    Procedimento: {procedimento}
    Glosa: R$ 00.00
    Pagamento do convenio: R$ {self.custo_atendimento:.2f}

            '''
        elif procedimento.lower() == 'Autorizado' and pagamento_convenio == False:
            return f''' {atendimento}
    Procedimento: {procedimento}
    Glosa: R$ {glosa:.2f}
    Pagamento do convenio: R$ 00.00

            '''
        elif procedimento.lower() == 'Negado':
            return f''' {atendimento}
    Procedimento: {procedimento}
    Glosa: R$ 00.00
    Pagamento do convenio: R$ 00.00

            '''