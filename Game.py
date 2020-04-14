import pygame
import os
import neat
import random
import math
pygame.font.init()

WIN_WIDTH = 800
WIN_HEIGHT = 600

STAT_FONT = pygame.font.SysFont("comicsans", 50)

class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 25
        self.height = 25
        self.change_x = (-1)**random.randrange(2) * 5
        self.change_y = (-1)**random.randrange(2) * 5
        self.score = 0

        self.colour = (255, 255, 255)

    def draw(self, window):
        pygame.draw.rect(window, self.colour, (self.x, self.y, self.width, self.height))
        self.x += self.change_x
        self.y += self.change_y

    def collision(self, paddle):
        if self.x > WIN_WIDTH - self.width or self.x < 0:
            self.change_x *= -1
        elif self.y < 0:
            self.change_y *= -1
        elif self.y > WIN_HEIGHT:
            pygame.quit()
            quit()
        if self.y - self.height < paddle.y + paddle.height and self.y + self.height > paddle.y:
            if self.x + self.width > paddle.x and self.x - self.width < paddle.x + paddle.width:
                self.change_y *= -1
                self.change_x *= (-1)**random.randrange(2)
                self.score += 1


class Paddle:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.vx = 0
        self.speed = speed
        self.width = 150
        self.height = 10
        self.colour = (255, 255, 255)

    def draw(self, window):
        pygame.draw.rect(window, self.colour, (self.x, self.y, self.width, self.height))

    def handle_keys(self):
        """ Handles Keys """
        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT]: # right key
            self.x += self.speed # move right
        elif key[pygame.K_LEFT]: # left key
            self.x -= self.speed # move left


def draw_window(window, paddle, ball):
    window.fill((0, 0, 0))
    text = STAT_FONT.render("Score: " + str(ball.score), 1, (255, 255, 255))
    window.blit(text, (WIN_WIDTH - 10 - text.get_width(), 10))
    paddle.draw(window)
    ball.draw(window)
    ball.collision(paddle)
    pygame.display.update()


def main():
    ball = Ball(400, 300)
    paddle = Paddle(400, WIN_HEIGHT-10, 5)
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    clock = pygame.time.Clock()

    score = 0

    run = True
    while run:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
        paddle.handle_keys()
        draw_window(win, paddle, ball)

main()
