WIDTH=700
HEIGHT=600

explorador = Actor('explorador-resize')
explorador.velocidade = 2

def draw():
    screen.fill((200, 100, 0))
    explorador.draw()

def update():
    if keyboard.left or keyboard.a:
        explorador.image = 'explorador-resize-esquerda'
        explorador.x -= 1 * explorador.velocidade
    if keyboard.right or keyboard.d:
        explorador.image = 'explorador-resize'
        explorador.x += 1 * explorador.velocidade
    if keyboard.up or keyboard.w: 
        explorador.y -= 1 * explorador.velocidade
    if keyboard.down or keyboard.s:
        explorador.y += 1 * explorador.velocidade


        

    
