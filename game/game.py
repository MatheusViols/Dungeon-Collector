from mago import Mago
from aranha import Aranha

WIDTH=700
HEIGHT=600

fim_jogo = False

mago = Mago()

aranha = Aranha()

jogador = Actor('explorador-resize') 
jogador.vidas = 3
jogador.velocidade = 3
jogador.vulneravel = True
jogador.olhando_direita = True

def atualizar_imagem_jogador():
    if not jogador.vulneravel:
        jogador.image = 'explorador-dano'
    elif jogador.olhando_direita:
        jogador.image = 'explorador-resize'
    else:
        jogador.image = 'explorador-resize-esquerda'


def mover_jogador():
    if keyboard.d or keyboard.right:
        jogador.olhando_direita = True
        jogador.x += jogador.velocidade

    if keyboard.a or keyboard.left:
        jogador.olhando_direita = False
        jogador.x -= jogador.velocidade

    if keyboard.w or keyboard.up:
        jogador.y -= jogador.velocidade

    if keyboard.s or keyboard.down:
        jogador.y += jogador.velocidade

def jogador_atingido():
    global fim_jogo

    if not jogador.vulneravel:
        return

    if jogador.colliderect(aranha.actor) or jogador.colliderect(mago.actor):
        jogador.vidas -= 1
        if jogador.vidas <= 0:
            fim_jogo = True

        jogador.vulneravel = False
        clock.schedule(jogador_vulneravel, 0.3)

def jogador_vulneravel():
    jogador.image = 'explorador-resize'
    jogador.vulneravel = True
    


def draw():
    if fim_jogo:
        screen.clear()
        screen.draw.text("GAME OVER", center=(WIDTH/2, HEIGHT/2), fontsize=100, color='white')
        return
    screen.fill((200, 100, 0))
    screen.draw.text(f"Vidas: {jogador.vidas}", topleft=(10,10), fontsize=30, color='white')
    jogador.draw()
    mago.actor.draw()
    aranha.actor.draw()

def update():
    if fim_jogo: 
        return

    mover_jogador()
    mago.mover()
    aranha.mover()
    jogador_atingido()
    atualizar_imagem_jogador()




    

        

    
