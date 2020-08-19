import pygame, math, time

#constantes
SCREEN_SIZE = (250, 250)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
POINTER_WATCH_SIZE = 125

OFFSET_X, OFFSET_Y = 125, 125

#inicialização da janela gráfica
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)

#carrega imagem do relógio
clockImage = pygame.image.load('relogio.jpg')

#inicializando valores trigonométricos
angle_radians = math.radians(90)
x = OFFSET_X + math.cos(angle_radians) * POINTER_WATCH_SIZE
y = OFFSET_Y - math.sin(angle_radians) * POINTER_WATCH_SIZE

#inicializa contador do tempo
time_before = time.time()

#loop do jogo
while True:

    screen.blit(clockImage, (0, 0))

    #pega novo instante de tempo
    time_after = time.time()

    #se passou 1 segundo, atualiza o ponto no perímetro
    if(time_after - time_before > 1.0):
        #atualizando valores trigonométricos
        angle_radians -= math.radians(6.0)
        x = OFFSET_X + math.cos(angle_radians) * POINTER_WATCH_SIZE
        y = OFFSET_Y - math.sin(angle_radians) * POINTER_WATCH_SIZE

        time_before = time.time()

    #desenhar o ponto central desse círculo
    #pygame.draw.rect(screen, RED, (OFFSET_X, OFFSET_Y, 5, 5))

    #desenhar o ponto que "anda" pelo perímetro
    #pygame.draw.rect(screen, RED, (x, y, 5, 5))

    #desenha o ponteiro dos segundos
    pygame.draw.lines(screen, BLUE, False, [(OFFSET_X, OFFSET_Y), (x, y)])

    #captura eventos (estamos preocupados com sair do jogo)
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break

    #atualizar gráficos da tela
    pygame.display.update()

    #preencher a superfície de fundo da janela gráfica com uma cor escura
    screen.fill(pygame.Color(0, 0, 0, 0))

pygame.quit()
