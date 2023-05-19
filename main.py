import pygame

SPRITE_RESOLUTION = (100, 100)
class GameSprite(sprite.Sprite):
    def __init__(self, x, y, filename, speed, resolution = SPRITE_RESOLUTION):
        super().__init__()
        self.image = transform.scale(image.load(filename), resolution)
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

    def colliderect(self, rect):
         return self.rect.colliderect(rect)

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()

        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 615:
            self.rect.y += self.speed
        
class Ball(GameSprite):
    def __init__(self, x, y, filename, speed, resolution=SPRITE_RESOLUTION):
        super().__init__(x, y, filename, speed, resolution)
        self.speed.x = speed
        self.speed.y = speed

    def update(self):

        if not (self.rect.x > 5 and self.rect.x < 1175):
            self.speed.x *= -1
        if not (self.rect.y > 5 and self.rect.y < 615):
            self.speed.y *= -1

        self.rect.x += self.speed.x
        self.rect.y += self.speed.y

RESOLUTION = (1280, 720)
window = display.set_mode(RESOLUTION)
window.fill(255, 255, 255)

player_1 = Player(0, 310, "racket.png", 5)
player_1 = Player(1270, 310, "racket.png", 5)

ball = Ball(590, 310, "ball.png", 5)

game = True
finish = False
score = 0
while game:

    for e in event.get():
        if e.type == QUIT:
            game = False

    if not finish:
        #window.blit(background, (0, 0))

        player_1.reset()
        player_2.reset()
        ball.reset()

        player_1.update()
        player_2.update()
        ball.update()
    
    
    display.update()    
