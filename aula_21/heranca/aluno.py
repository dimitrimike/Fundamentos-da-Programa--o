from pessoa import Pessoa
# NOME, CPF, DATA DE NASCIMENTO, ANO DE INGRESSO, NOTAS, MATRICULA E SE ESTA ATIVO OU NÃO
class Aluno(Pessoa): # Subclasse, pois recebe herança
    def __init__(self, nome: str, cpf: str, data_nascimento: str, ano_ingresso: int, matriculoa: str):
        super().__init__(nome, cpf, data_nascimento)
        self.ano_ingresso = ano_ingresso
        self.matricula = self.matricula
        self.ativo = True
        self.notas = []

    # Métodos de Notas
    def adicionar_notas(self, disciplina: str, notas: float):
    # Nota precisa estar entre 0 e 10
        if not(0 <= nota <= 10): 
            raise ValueError("Nota deve estar entre 0 e 10.")
        
        if disciplina not in self.notas:
            self.notas[disciplina] = []

        self.notas[disciplina].append(nota)