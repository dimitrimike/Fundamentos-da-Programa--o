# Classe Filha - Subclass

from paciente import Paciente


class PacienteParticular(Paciente):
    def __init__(self, nome: str, data_nascimento: str, cpf: str, telefone: str, tipo_sanguineo: str, numero_prontuario: str, forma_pagamento: str, desconto_fidelidade: str):
        super().__init__(nome, data_nascimento, cpf, telefone, tipo_sanguineo, numero_prontuario)
        self.forma_pagamento = forma_pagamento
        self.desconto_fidelidade = desconto_fidelidade

    def exibir_informacoes(self):
        informacoes_paciente = super().exibir_informacoes(detalhado=True)
        return f''' {informacoes_paciente}
    Forma de pagamento: {self.forma_pagamento}
    Possui desconto de fidelidade: {self.desconto_fidelidade}

        '''

    def calcular_valor_final(self, taxa_urgencia: float = 50.0):
        self.taxa_urgencia = taxa_urgencia
        if 'urgente' in self.tipo_atendimento.lower():
            self.taxa_urgencia = taxa_urgencia
        else:
            self.taxa_urgencia = 0.0
        if self.desconto_fidelidade.lower() == 'sim':
            self.desconto_fidelidade = 0.1
        else:
            self.desconto_fidelidade = 0.0
        valor_final = self.custo_atendimento - (self.desconto_fidelidade * self.custo_atendimento) + self.taxa_urgencia
        return f''' --- Conta do paciente {self.nome} ---

    Custo do atendimento: R$ {self.custo_atendimento:.2f}
    Desconto de fidelidade: R$ {self.desconto_fidelidade * self.custo_atendimento:.2f}
    Taxa de urgência: R$ {self.taxa_urgencia:.2f}

    Total a pagar: R$ {valor_final:.2f}

        '''


