from pgzero.actor import Actor

class Aranha():

    def __init__(self):
        self.actor = Actor('aranha', (351, 81))
        self.velocidade = 1.5 
        self.limite_cima = 81
        self.limite_baixo = 189

    def mover(self):
        self.actor.y += self.velocidade

        if self.actor.y >= self.limite_baixo or self.actor.y <= self.limite_cima: 
            self.velocidade = -self.velocidade
