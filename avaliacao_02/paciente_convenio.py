# Classe Filha - Subclass

from paciente import Paciente

class PacienteConvenio(Paciente):
    def __init__(self, nome: str, data_nascimento: str, cpf: str, telefone: str, tipo_sanguineo: str, numero_prontuario: str, nome_convenio: str, numero_carteirinha: str):
        super().__init__(nome, data_nascimento, cpf, telefone, tipo_sanguineo, numero_prontuario)
        self.nome_convenio = nome_convenio
        self.numero_carteirinha = numero_carteirinha

    
    def registrar_autorizacao(self, pagamento_convenio: str):
        procedimento = super().registrar_atendimento(self.tipo_atendimento, self.custo_atendimento)
        pagamento = pagamento_convenio.lower()

        if pagamento == 'confirmado':
            return f''' {procedimento}
    Repasse do convênio {self.nome_convenio}: {pagamento}
    Glosa: R$ 0.00

    '''
        elif pagamento == 'negado':
            return f''' {procedimento}
    Repasse do cônvenio {self.nome_convenio}: {pagamento}
    Glosa: R$ {self.custo_atendimento}

    '''
        else:
            raise ValueError("Erro! Para confirmar o repasse do convênio digite: 'confirmado' ou 'negado'.")
        

    def exibir_informacoes_convenio(self):
        informacoes_paciente = super().exibir_informacoes(detalhado=True)
        return f''' {informacoes_paciente}
    Nome do convenio: {self.nome_convenio}
    Número da carteirinha: {self.numero_carteirinha}

    '''