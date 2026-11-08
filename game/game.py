from mago import Mago
from aranha import Aranha
from mapa import Mapa

WIDTH=756
HEIGHT=648

fim_jogo = False
TEMPO_INICIAL = 30
tempo_restante = TEMPO_INICIAL

mapa = Mapa()

mago = Mago()

aranha = Aranha()

jogador = Actor('explorador-resize', (75,75)) 
jogador.vidas = 3
jogador.vulneravel = True
jogador.olhando_direita = True
jogador.em_movimento = False
jogador.contador_baus = 0

def atualizar_imagem_jogador():
    if not jogador.vulneravel:
        jogador.image = 'explorador-dano'
    elif jogador.olhando_direita:
        jogador.image = 'explorador-resize'
    else:
        jogador.image = 'explorador-resize-esquerda'


def parar_movimento():
    jogador.em_movimento = False

def mover_jogador():
    if jogador.em_movimento:
        return

    direcao_x, direcao_y = 0, 0

    if keyboard.d or keyboard.right:
        jogador.olhando_direita = True
        direcao_x = 1

    if keyboard.a or keyboard.left:
        jogador.olhando_direita = False
        direcao_x = -1

    if keyboard.w or keyboard.up:
        direcao_y = -1

    if keyboard.s or keyboard.down:
        direcao_y = 1

    novo_x = jogador.x + (direcao_x * mapa.tamanho_tile)
    novo_y = jogador.y + (direcao_y * mapa.tamanho_tile) 

    if mapa.andavel(novo_x, novo_y, WIDTH, HEIGHT):
        jogador.em_movimento = True
        animate(jogador, pos=(novo_x, novo_y), duration=0.25, tween="linear", on_finished=parar_movimento)



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

def coletar_baus():
    for bau in mapa.baus:
        if not bau.aberto and jogador.colliderect(bau.actor):
            bau.abrir()
            jogador.contador_baus += 1


def draw():
    if fim_jogo:
        screen.clear()
        screen.draw.text("GAME OVER", center=(WIDTH/2, HEIGHT/2), fontsize=100, color='white')
        return

    mapa.draw(screen)
    screen.draw.text(f"VIDAS: {jogador.vidas}", midleft=(15,27), fontsize=30, color='white')
    screen.draw.text(f"BAUS: {jogador.contador_baus}", center=(378,27), fontsize=30, color='white')
    screen.draw.text(f"TEMPO: {int(tempo_restante)}", midright=(741,27), fontsize=30, color='white')
    jogador.draw()
    mago.actor.draw()
    aranha.actor.draw()
    for bau in mapa.baus:
        bau.actor.draw()

def update(dt):
    global tempo_restante, fim_jogo

    if fim_jogo: 
        return

    tempo_restante -= dt 
    if tempo_restante <= 0:
        fim_jogo = True
        return

    mover_jogador()
    mago.mover()
    aranha.mover()
    coletar_baus()
    jogador_atingido()
    atualizar_imagem_jogador()


    
