class Eletrodomestico:
    def __init__(self, cor, potencia, voltagem, preco):
        self.cor = cor
        self.potencia = potencia
        self.voltagem = voltagem
        self.preco = preco
        self.ligado = False
        self.amperagem_atual_no_motor = 0

    def desligar(self):
        self.__ligado = False

    def esta_ligado(self):
        return self.__ligado
        