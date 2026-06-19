class Pessoa:
    # Constructor
    def __init__(self, nome: str, cpf: str, data_nascimento: str):
        self.nome = nome      # atributo público
        self._cpf = cpf       # atributo privado
        self.data_nascimento = data_nascimento # Atributo público

    # Método de apresentação
    def apresentar(self) -> str:
        return f"Olá, meu nome é {self.nome}."


# ── Criação de OBJETOS (instâncias) ────────────────────────
pessoa1 = Pessoa("Ana Lima", "123")
pessoa2 = Pessoa("Bruno Costa", "987")

print(pessoa1.apresentar())  # Olá, meu nome é Ana Lima.
print(pessoa2.apresentar())  # Olá, meu nome é Bruno Costa.
print(type(pessoa1))         # <class '__main__.Pessoa'>