from pgzero.actor import Actor

class Mago():
    def __init__(self):
        self.actor = Actor('mago-direita', (200, 300))
        self.velocidade = 2
        self.limite_direita = 300
        self.limite_esquerda = 100


    def mover(self):
        self.actor.x += self.velocidade

        if self.actor.x <= self.limite_esquerda:
            self.actor.image = 'mago-direita'
            self.velocidade = abs(self.velocidade)
        elif self.actor.x >= self.limite_direita:
            self.actor.image = 'mago-esquerda'
            self.velocidade = -abs(self.velocidade)


        

