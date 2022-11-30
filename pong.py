import pygame, sys

#kommentarer är på svengelska

class Ball:
    def __init__(self, screen, color, posX, posY, radius):
        self.screen = screen
        self.color = color
        self.posX = posX
        self.posY = posY
        self.dx = 0
        self.dy = 0
        self.radius = radius
        self.show()        
    
    def show(self):
        pygame.draw.circle(self.screen, self.color, (self.posX, self.posY), self.radius)

    def startMoving(self):
        self.dx = 0.3
        self.dy = 0.1

    def move(self):
        self.posX += self.dx
        self.posY += self.dy

class Paddle:
    def __init__(self, screen, color, posX, posY, width, heigth):
        self.screen = screen
        self.color = color
        self.posX = posX
        self.posY = posY
        self.width = width
        self.heigth = heigth
        self.state = 'stanna'
        self.show()

    def show(self):
        pygame.draw.rect(self.screen, self.color, (self.posX, self.posY , self.width, self.heigth))

    def move(self):
        if self.state == 'up':
            self.posY -= 0.3
        if self.state == 'down':
            self.posY += 0.3
        
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

#saker/obejkt
ball = Ball(screen, WHITE, WIDTH//2, HEIGHT//2, 10)
paddle = Paddle(screen, WHITE, 10, HEIGHT//2 -60 , 20, 120)
paddle2 = Paddle(screen, WHITE, WIDTH -30, HEIGHT//2 -60, 20, 120)

#Variabler
spelar = False

#mainloop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p: 
                ball.startMoving()
                spelar = True
            
            if event.key == pygame.K_w:
                paddle.state = 'up'
            if event.key == pygame.K_s:
                paddle.state = 'down'
            if event.key == pygame.K_UP:
                paddle2.state = 'up'
            if event.key == pygame.K_DOWN:
                paddle2.state = 'down'
        if event.type == pygame.KEYUP:
            paddle.state = 'stanna'
            paddle2.state = 'stanna'


    if spelar:
        paint_black()
        ball.move()
        ball.show()

        paddle.show()
        paddle.move()
        paddle2.show()
        paddle2.move()

    pygame.display.update()