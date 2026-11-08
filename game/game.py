from jogador import Jogador
from mago import Mago
from aranha import Aranha
from mapa import Mapa

WIDTH=756
HEIGHT=648

ganhou_jogo = False
fim_jogo = False
TEMPO_INICIAL = 30
tempo_restante = TEMPO_INICIAL

mapa = Mapa()

jogador = Jogador(mapa)

mago = Mago()

aranha = Aranha()

music.play('trilha')

def reiniciar_jogo():
    global fim_jogo, ganhou_jogo, tempo_restante, mapa, jogador, mago, aranha

    ganhou_jogo = False
    fim_jogo = False
    tempo_restante = 30

    mapa = Mapa()
    jogador = Jogador(mapa)
    mago = Mago()
    aranha = Aranha()
    
def contar_baus():
    global ganhou_jogo

    if jogador.contador_baus == len(mapa.baus):
        ganhou_jogo = True

def contar_vidas():
    global fim_jogo
    
    if jogador.vidas == 0:
        fim_jogo = True

def draw():
    if ganhou_jogo or fim_jogo:
        texto_personalizado = "GAME OVER" if fim_jogo else "DUNGEON EXPLORADA!"
        mensagem = f"{texto_personalizado}\nAperte R para reiniciar"

        screen.clear()
        screen.draw.text(mensagem, center=(WIDTH/2, HEIGHT/2), fontsize=50, color='white')

        return

    mapa.draw(screen)
    for bau in mapa.baus:
        bau.actor.draw()
    screen.draw.text(f"VIDAS: {jogador.vidas}", midleft=(15,27), fontsize=30, color='white')
    screen.draw.text(f"BAUS: {jogador.contador_baus}", center=(378,27), fontsize=30, color='white')
    screen.draw.text(f"TEMPO: {int(tempo_restante)}", midright=(741,27), fontsize=30, color='white')

    jogador.actor.draw()
    mago.actor.draw()
    aranha.actor.draw()

def update(dt):
    global tempo_restante, fim_jogo

    if ganhou_jogo:
        return
    elif fim_jogo: 
        return

    tempo_restante -= dt 
    if tempo_restante <= 0:
        fim_jogo = True
        return

    mover_jogador()

    mago.mover()
    aranha.mover()

    if jogador.foi_atingido((mago, aranha)):
        jogador.levar_dano()
        clock.schedule(jogador.ficar_vulneravel, 0.3)

    jogador.atualizar_imagem()

    jogador.coletar_baus()
    contar_baus()
    contar_vidas()


def mover_jogador():

    direcao_x, direcao_y = 0, 0

    if keyboard.d or keyboard.right:
        direcao_x = 1

    if keyboard.a or keyboard.left:
        direcao_x = -1

    if keyboard.w or keyboard.up:
        direcao_y = -1

    if keyboard.s or keyboard.down:
        direcao_y = 1

    jogador.mover(direcao_x, direcao_y)

def on_key_down(key):
    if key == keys.R:
        reiniciar_jogo()
        

    
