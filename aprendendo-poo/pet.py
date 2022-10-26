# nome, espécie, idade, humano
class Pet:
    def __init__(self, nome, idade, especie, dono):
        self.nome = nome
        self.idade = idade
        self.especie = especie
        self.dono = dono
    
# o método str muda a visualização dos dados de uma instância da classe
    def __str__(self):
       return f"""
       - Espécie: {self.especie}
       - Nome: {self.nome}
       - Idade: {self.idade}
       """

thor = Pet('Thor', 'Gato', 5, 'Juliana')
print(thor)