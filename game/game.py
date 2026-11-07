from mago import Mago
from aranha import Aranha

WIDTH=700
HEIGHT=600

mago = Mago()

aranha = Aranha()

jogador = Actor('explorador-resize') 
jogador.velocidade = 3

def mover_jogador():
    if keyboard.d or keyboard.right:
        jogador.image = 'explorador-resize'
        jogador.x += jogador.velocidade

    if keyboard.a or keyboard.left:
        jogador.image = 'explorador-resize-esquerda'
        jogador.x -= jogador.velocidade

    if keyboard.w or keyboard.up:
        jogador.y -= jogador.velocidade

    if keyboard.s or keyboard.down:
        jogador.y += jogador.velocidade


def draw():
    screen.fill((200, 100, 0))
    jogador.draw()
    mago.actor.draw()
    aranha.actor.draw()

def update():
    mover_jogador()
    mago.mover()
    aranha.mover()




    

        

    
