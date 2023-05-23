import pygame
import math
from asteroides import*
#inicializando o  pygame e criando a janela
pygame.init()
display = pygame.display.set_mode([1070, 580])
pygame.display.set_caption("Rigil Kentaurus")
def draw():
    display.blit(fundo, (0, 0))
    display.blit(nave, (x,y))
    display.blit(nave2, (x2,y2))

gameloop = True
clock = pygame.time.Clock()
i = 0
x = 450
y = 459
x2 = 0
y2 = 0
velocidade = 5
velocidade2 = 5
timer = 0
numero_asteroides = 7
fundo = pygame.image.load('universo.png')

nave3 = pygame.image.load('nave espacial.png')
nave = pygame.image.load('nave espacial.png')
nave2 = pygame.image.load('nave.png')
font = pygame.font.SysFont('Arial', 30)
def rotacao(nave,angulo):
    return pygame.transform.rotate(nave,angulo)


#text = font.render('Bem-Vindo ao Jogo de Astrofisica!', True, (255, 255, 255))
#textRect = text.get_rect()
#textRect.center = (1070//2, 580//2)
#musica
pygame.mixer.music.load('battleThemeA.wav')
pygame.mixer.music.play(-1)
#sons
shoot = pygame.mixer.Sound('burst-fire.wav')
if __name__ == "__main__":
    while gameloop:
        clock.tick(90)
        #display.blit(text, textRect)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #botão de fechar o jogo
                gameloop = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    shoot.play()
        timer += 0.01
        x2 = 450 + math.sin(timer) * 200
        keys = pygame.key.get_pressed() #fila de todos as teclas do teclado que estão sendo pressionadas
        if keys[pygame.K_LEFT]:
            nave = rotacao(nave3, 90)
            if x <= 0:
                x = 0
            else:
                x -= velocidade
        elif keys[pygame.K_RIGHT]:
            nave = rotacao(nave3, -90)
            if x >= 1070-125:
                x = 1070-125
            else:
                x += velocidade

        elif keys[pygame.K_UP]:
            nave = rotacao(nave3, 0)
            if y <= 0:
                y = 0
            else:
                y -= velocidade
        elif keys[pygame.K_DOWN]:
            nave = rotacao(nave3, 180)
            if y >= 580 - 125:
                y = 580 - 125
            else:
                y += velocidade


        draw()
        pygame.display.update()