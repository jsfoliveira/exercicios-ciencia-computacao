class Tv():
    def __init__(self, volume, canal, tamanho):
        self.__volume = 50
        self.canal = 1
        self.tamanho = tamanho
        self.ligado = False
    
    def aumenta_volume(self):
        self.__volume += 1
    
    def diminui_volume(self):
        self.__volume -= 1

    def modificar_canal(self, canal):
        if canal < 1 or canal >= 99:
            raise ValueError('Canal indisponível')
        self.canal = canal
    
    def ligar_desligar(self):
        self.ligado = not self.ligado
    