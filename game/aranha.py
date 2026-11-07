from pgzero.actor import Actor

class Aranha():

    def __init__(self):
        self.actor = Actor('aranha', (400, 100))
        self.velocidade = 2.3
        self.limite_cima = 50
        self.limite_baixo = 150

    def mover(self):
        self.actor.y += self.velocidade

        if self.actor.y >= self.limite_baixo or self.actor.y <= self.limite_cima: 
            self.velocidade = -self.velocidade
