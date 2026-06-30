# Classe Filha - Subclass

from paciente import Paciente

class PacienteParticular(Paciente):
    def __init__(self, nome, data_nascimento, cpf, telefone, tipo_sanguineo, numero_prontuario, forma_pagamento, desconto_fidelidade):
        super().__init__(nome, data_nascimento, cpf, telefone, tipo_sanguineo, numero_prontuario)
        self.forma_pagamento = forma_pagamento
        self.desconto_fidelidade = desconto_fidelidade

    def exibir_informacoes(self):
        informacoes_paciente = super().exibir_informacoes()
        return f''' {informacoes_paciente}
    Forma de pagamento: {self.forma_pagamento}
    Desconto de fidelidade: {self.desconto_fidelidade}

        '''