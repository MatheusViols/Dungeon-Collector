from pgzero.actor import Actor

class Bau():
    def __init__(self, posicao):
        self.aberto = False
        self.actor = Actor('bau-fechado', posicao)

    def abrir(self):
        self.aberto = True
        self.actor.image = 'bau-aberto'

    



