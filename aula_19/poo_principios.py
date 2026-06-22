# Precisamos criar um molde de uma pessoa => class
# Características => atributos -> varáveis, nome e cpf
# Ações => métodos -> funções

class Pessoa:
    def __init__(self, nome: str, cpf: str):
        self.nome = nome      # atributo público
        self._cpf = cpf       # atributo privado (convenção)

    def apresentar(self) -> str:
        return f"Olá, meu nome é {self.nome}."


# ── Criação de OBJETOS (instâncias) ────────────────────────
pessoa1 = Pessoa("Ana Lima", "123.456.789-00")
pessoa2 = Pessoa("Bruno Costa", "987.654.321-00")

print(pessoa1.apresentar())  # Olá, meu nome é Ana Lima.
print(pessoa2.apresentar())  # Olá, meu nome é Bruno Costa.
print(type(pessoa1))         # <class '__main__.Pessoa'>