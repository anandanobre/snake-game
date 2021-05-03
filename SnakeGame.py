#Snake Game(Jogo da cobrinha)

import pygame
import random

pygame.init()

# Difinição de cores
background = (23, 21, 30)
snake_color = ( 116, 78, 202)
food_color = (255, 254, 254)
cinza = (193, 193, 193)

# Definição da fonte
font = pygame.font.SysFont("hack", 35)

# Cria a tela
dimensoes = (600, 600)
screen = pygame.display.set_mode((dimensoes))
pygame.display.set_caption('Snake Game')
screen.fill(background)

# Cria clock
clock = pygame.time.Clock()

# Valore iniciais da cobra
x = 300
y = 300
block_size = 30 # Tamanho do quadrado
snake = [[x, y]]
dx = 0
dy = 0

# Gera posição aleatória da comida
x_comida = round(random.randrange(0, 600 - block_size) / 30) * 30
y_comida = round(random.randrange(0, 600 - block_size) / 30) * 30


# Função que desenha a cobra
def draw_snake(snake):
    screen.fill(background) # Define a cor de fundo da tela
    for i in snake:
        pygame.draw.rect(screen, snake_color, [i[0], i[1], block_size, block_size]) # Desenha a cobra na tela

# Função que controla a cobra
def move(dx, dy, snake):
    for event in pygame.event.get():
        # Detecta se o evento é igual a uma tecla precionada e direciona a cobra dependendo de qual tecla for
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dx = - block_size
                dy = 0
            elif event.key == pygame.K_RIGHT:
                dx = block_size
                dy = 0
            elif event.key == pygame.K_UP:
                dx = 0
                dy = - block_size
            elif event.key == pygame.K_DOWN:
                dx = 0
                dy = block_size
    x_novo = snake[-1][0] + dx
    y_novo = snake[-1][1] + dy
    snake.append([x_novo, y_novo])
    del snake[0]
    return dx, dy, snake

# Função cria comida
def food(dx, dy, x_comida, y_comida, lista_cobra):
    head = snake[-1]
    x_novo = head[0] + dx
    y_novo = head[1] + dy
    if head[0] == x_comida and head[1] == y_comida:
        snake.append([x_novo, y_novo])
        x_comida = round(random.randrange(0, 600 - block_size) / 30) * 30
        y_comida = round(random.randrange(0, 600 - block_size) / 30) * 30

    pygame.draw.rect(screen, food_color, [x_comida, y_comida, block_size, block_size]) # Desenha a comida na tela
    return x_comida, y_comida, snake

# Função cria paredes
def wall(snake):
    head = snake[-1]
    x = head[0]
    y = head[1]

    if x not in range(700) or y not in range(700):
        raise Exception

# Função verifica se a cobra se moredeu
def bit_itself(snake):
    head = snake[-1]
    body = snake.copy()

    del body[-1]
    for x, y in body:
        if x == head[0] and y == head[1]:
            raise Exception

# Função conta pontuação
def scores(snake):
    pts = str(len(snake)-1)
    score = font.render("Score: " + pts, True, cinza)
    screen.blit(score, [0, 0])


# Loop que controla o jogo
while True:
    pygame.display.update()
    draw_snake(snake)
    dx, dy, snake = move(dx, dy, snake)
    x_comida, y_comida, snake = food(dx, dy, x_comida, y_comida, snake)
    print(snake)
    wall(snake)
    bit_itself(snake)
    scores(snake)
    clock.tick(5) # FPS do jogo
