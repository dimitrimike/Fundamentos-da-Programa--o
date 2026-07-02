# Classe Filha - Subclass

from paciente import Paciente


class PacienteParticular(Paciente):
    def __init__(self, nome: str, data_nascimento: str, cpf: str, telefone: str, tipo_sanguineo: str, numero_prontuario: str, forma_pagamento: str, desconto_fidelidade: str):
        super().__init__(nome, data_nascimento, cpf, telefone, tipo_sanguineo, numero_prontuario)
        self.forma_pagamento = forma_pagamento
        self.desconto_fidelidade = desconto_fidelidade


    def calcular_valor_final(self):
        registro_atendimento = super().registrar_atendimento(self.tipo_atendimento, self.custo_atendimento)
        valor_consulta = 100.00
        taxa_urgencia = 50.00
        if self.desconto_fidelidade.lower() == 'sim':
            desconto = 0.5
        elif self.desconto_fidelidade.lower() == 'não':
            desconto = 0
        else:
            raise ValueError("Erro! Para informar se o paciente tem desconto fidelidade digite: 'sim' ou 'não'.")
        valor_consulta_desconto = valor_consulta - (valor_consulta * desconto)
        valor_final = self.custo_atendimento + valor_consulta_desconto
        valor_final_urgencia = valor_final + taxa_urgencia
        if 'urgente' in self.tipo_atendimento.lower():
            return f'''--- Conta do Paciente {self.nome} ---

    Tipo de atendimento: {self.tipo_atendimento}
    Custo do atendimento: {self.custo_atendimento}
    Desconto Fidelidade: {self.desconto_fidelidade}
    Consulta: R$ {valor_consulta_desconto:.2f}
    Taxa de Urgência: R$ {taxa_urgencia:.2f}
    Total: R$ {valor_final_urgencia:.2f}

    '''
        else:
            return f'''--- Conta do Paciente {self.nome} ---

    Tipo de atendimento: {self.tipo_atendimento}
    Custo do atendimento: {self.custo_atendimento}
    Desconto Fidelidade: {self.desconto_fidelidade}
    Consulta: R$ {valor_consulta_desconto:.2f}
    Total: R$ {valor_final:.2f}

    '''

    def exibir_informacoes_particular(self):
        informacoes_paciente_det = super().exibir_informacoes(detalhado=True)
        return f''' {informacoes_paciente_det}
    Forma de pagamento: {self.forma_pagamento}
    Possui desconto de fidelidade: {self.desconto_fidelidade}

    '''