import pygame, sys

class Ball:
    def __init__(self, screen, color, posX, posY, radius):
        self.screen = screen
        self.color = color
        self.posX = posX
        self.posY = posY
        self.radius = radius
        self.show()
        
    
    def show(self):
        pygame.draw.circle(self.screen, self.color, (self.posX, self.posY), self.radius)

class Paddle:
    def __init__(self, screen, color, posX, posY, width, heigth):
        self.screen = screen
        self.color = color
        self.posX = posX
        self.posY = posY
        self.width = width
        self.heigth = heigth
        self.show()

    def show(self):
        pygame.draw.rect(self.screen, self.color, (self.posX, self.posY , self.width, self.heigth))

#heja
pygame.init()

WIDTH, HEIGHT = 900,500
BLACK = (0,0,0)
WHITE = (255,255,255)

screen = pygame.display.set_mode((WIDTH, HEIGHT) )
pygame.display.set_caption('Ping pong')

def paint_black():
    screen.fill(BLACK)
    pygame.draw.line(screen, WHITE, (WIDTH//2,0), (WIDTH//2,HEIGHT),5)

paint_black()

#saker
ball = Ball(screen, WHITE, WIDTH//2, HEIGHT//2, 10)
paddle = Paddle(screen, WHITE, 10, HEIGHT//2 -60 , 20, 120)



#mainloop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.update()