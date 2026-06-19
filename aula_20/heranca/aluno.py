from pessoa import Pessoa
# NOME, CPF, DATA DE NASCIMENTO, ANO DE INGRESSO, NOTAS, MATRICULA E SE ESTA ATIVO OU NÃO
class Aluno(Pessoa):
    def __init__(self, nome: str, cpf: str, data_nascimento: str, ano_ingresso: int, matriculoa: str):
        super().__init__(nome, cpf, data_nascimento)
        self.ano_ingresso = ano_ingresso
        self.matricula = self.matricula
        self.ativo = True
        self.notas = []