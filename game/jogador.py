from pgzero.actor import Actor
from pgzero.animation import animate

class Jogador():
    def __init__(self, mapa):
        self.actor = Actor('explorador-direita', (75, 75))
        self.vidas = 3
        self.vulneravel = True
        self.olhando_direita = True
        self.em_movimento = False
        self.contador_baus = 0

        self.mapa = mapa

    def mover(self, direcao_x, direcao_y):
        if self.em_movimento:
            return

        if direcao_x >= 0:
            self.olhando_direita = True
        else:
            self.olhando_direita = False

        novo_x = self.actor.x + (direcao_x * self.mapa.tamanho_tile)
        novo_y = self.actor.y + (direcao_y * self.mapa.tamanho_tile) 

        if self.mapa.andavel(novo_x, novo_y):
            self.em_movimento = True
            animate(self.actor, pos=(novo_x, novo_y), duration=0.30, tween="linear", on_finished=self.parar_movimento)

    def atualizar_imagem(self):
        if not self.vulneravel:
            self.actor.image = 'explorador-dano'
        elif self.olhando_direita:
            self.actor.image = 'explorador-direita'
        else:
            self.actor.image = 'explorador-esquerda'

    def parar_movimento(self):
        self.em_movimento = False

    def coletar_baus(self):
        for bau in self.mapa.baus:
            if not bau.aberto and self.actor.colliderect(bau.actor):
                bau.abrir()
                self.contador_baus += 1

    def foi_atingido(self, inimigos):
        if not self.vulneravel:
            return

        for inimigo in inimigos:
            if self.actor.colliderect(inimigo.actor): 
                return True

        return False

    def levar_dano(self):
        self.vidas -= 1
        self.vulneravel = False


    def ficar_vulneravel(self):
        self.vulneravel = True
        self.atualizar_imagem()

