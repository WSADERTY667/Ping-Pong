from pygame import *
from random import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_left_right, size_up_down, player_speed, who_are_you):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_left_right, size_up_down))
        self.speed = player_speed
        self.who_are_you = who_are_you
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

lost_1 = 0
lost_2 = 0


class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if self.who_are_you == 1:
            if keys[K_UP] and self.rect.y > 5:
                self.rect.y -= self.speed
            if keys[K_DOWN] and self.rect.y < win_height - 150:
                self.rect.y += self.speed
        if self.who_are_you == 2:
            if keys[K_w] and self.rect.y > 5:
                self.rect.y -= self.speed
            if keys[K_s] and self.rect.y < win_height - 150:
                self.rect.y += self.speed
        Sprite_x = self.rect.x
        Sprite_y = self.rect.y

        Sprite_center_x = self.rect.centerx
        Sprite_top = self.rect.top

player_1 = Player("Безымянный.png", 10, 200, 20, 150, 10, 1)
player_2 = Player("Безымянный.png", 970, 200, 20, 150, 10, 2)

font.init()
font2 = font.SysFont("Arial", 25)

win_width = 1000
win_height = 600
window = display.set_mode((win_width, win_height))
display.set_caption("Ping-Pong")
background = transform.scale(image.load("galaxy.jpg"), (win_width, win_height))

clock = time.Clock()
FPS = 90
game = True
finish = 1

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish == 1:
        window.blit(background,(0, 0))
        player_1.update()
        player_2.update()

        player_1.reset()
        player_2.reset()

    display.update()
    clock.tick(FPS)