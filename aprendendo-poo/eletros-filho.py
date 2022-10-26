from eletrodomesticos import Eletrodomestico


class Liquidificador(Eletrodomestico): # Exemplo de Herança
    def __init__(self, cor, potencia, voltagem, preco):
	# chamando o método da classe mãe
        super().__init__(cor, potencia, voltagem, preco)


class Geladeira(Eletrodomestico):
    def __init__(self, cor, potencia, voltagem, preco, quantidade_de_portas=1):
        super().__init__(cor, potencia, voltagem, preco)
	# sobrescrita do método da classe mãe
        self.quantidade_de_portas = quantidade_de_portas


    def __str__(self):
       return f"""
       - Cor: {self.cor}
       - Potência: {self.potencia}
       - Voltagem: {self.voltagem}
       - Preço: {self.preco}
       """

liquidificador = Geladeira("Azul", "110", "127", "200")
print(liquidificador)
