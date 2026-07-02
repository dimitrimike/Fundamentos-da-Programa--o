# Classe Pai - Classe Abstrata - SuperClass

class Paciente:
    def __init__(self,nome: str, data_nascimento: str, cpf: str, telefone: str, tipo_sanguineo: str, numero_prontuario: str):
        self.nome = nome
        self._data_nascimento = data_nascimento
        self._cpf = cpf
        self._telefone = telefone
        self.tipo_sanguineo = tipo_sanguineo
        self.numero_prontuario = numero_prontuario

    def registrar_atendimento(self, tipo_atendimento: str, custo_atendimento: float):
        self.tipo_atendimento = tipo_atendimento
        self.custo_atendimento = custo_atendimento
        return f'''  --- Atendimento Registrado ---

    Tipo de atendimento: {self.tipo_atendimento}
    Custo do atendimento: R$ {self.custo_atendimento:.2f}
    '''

    def exibir_informacoes(self, detalhado=False):
        if detalhado:
            return f'''--- Informações do Paciente (detalhado) ---

    Nome: {self.nome}
    Data de Nascimento: {self._data_nascimento}
    CPF: {self._cpf}
    Telefone: {self._telefone}
    Tipo sanguineo: {self.tipo_sanguineo}
    Prontuario: {self.numero_prontuario}
    '''
        else:
            return f''' --- Informações do Paciente ---

    Nome: {self.nome}
    Tipo sanguineo: {self.tipo_sanguineo}
    Prontuario: {self.numero_prontuario}
    '''



    