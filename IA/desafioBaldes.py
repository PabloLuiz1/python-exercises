
class Balde:
    def __init__ (self, capacidade):
        print ("Um balde com", capacidade, "litros de capacidade")
        self.capacidade = capacidade
        self.volumeAtual = 0

    def taCheio(self):
        if (self.volumeAtual == self.capacidade):
            return True
        else:
            return False

    def taVazio(self):
        if (self.volumeAtual == 0):
            return True
        else:
            return False

    def encher (self):
        if (self.taCheio()):
            print ("O balde ja esta cheio")
        else:
            self.volumeAtual = self.capacidade
            print ("Enchendo o balde ate sua capacidade maxima de", self.capacidade, "litros")

    def jogarFora (self):
        self.volumeAtual = 0

    def transferir (self, balde):
        if (balde.taCheio()):
            print ("O outro balde esta cheio, nao eh possivel trasnferir volume")
        elif (self.taVazio()):
            print ("Este balde esta vazio, nao eh possivel transferir volume")

balde4 = Balde(4)
balde2 = Balde(2)
balde4.encher()
balde2.encher()
