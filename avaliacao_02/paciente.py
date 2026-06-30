# Classe Pai - Classe Abstrata - SuperClass

class Paciente:
    def __init__(self,nome, data_nascimento, cpf, telefone, tipo_sanguineo, numero_prontuario):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.telefone = telefone
        self.tipo_sanquineo = tipo_sanguineo
        self.numero_prontuario = numero_prontuario

    
    def registrar_atendimento(self):
        return f'''
    Atendimento tipo: 
    Atendimento custo:
    '''

    def exibir_informacoes (self):
        return f'''
    Nome: {self.nome}
    Data de Nascimento: {self.data_nascimento}
    CPF: {self.cpf}
    Telefone: {self.telefone}
    Tipo sanguineo: {self.tipo_sanquineo}
    Prontuario: {self.numero_prontuario}
    '''