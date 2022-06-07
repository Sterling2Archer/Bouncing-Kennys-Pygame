import pygame
import random
import sys

pygame.init()
surface = pygame.display.set_mode((1000, 800))
color = (255, 255, 255)
surface.fill(color)
pygame.display.flip()

WIDTH = 1000
HEIGHT = 800
BACKGROUND = (255, 255, 255)


class Ball:
    def __init__(self):
        self.image = pygame.image.load(random.choice(("zombies-zombie-kenny.png", "other-alter-egos-me-kenny-2-cc.png")))
        self.speed = [random.uniform(-4, 4), 2]
        self.rect = self.image.get_rect()
        self.alive = True

    def update(self):
        if self.rect.top < 0:
            self.speed[1] = -self.speed[1]
            self.speed[0] = random.uniform(-4, 4)
        elif self.rect.left < 0 or self.rect.right > WIDTH:
            self.speed[0] = -self.speed[0]
        elif self.rect.bottom > HEIGHT:
            self.alive = False
        self.move()

    def move(self):
        self.rect = self.rect.move(self.speed)


def main():
    clock = pygame.time.Clock()
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    ball1 = Ball()
    ball2 = Ball()
    ball3 = Ball()
    ball4 = Ball()

    balls = [ball1, ball2, ball3, ball4]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                for ball in balls:
                    if ball.rect.collidepoint(pygame.mouse.get_pos()):
                        ball.speed[0] = random.randrange(-4, 4)
                        ball.speed[1] = -2
                        break
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill(BACKGROUND)
        for i, ball in enumerate(balls):
            if ball.alive:
                screen.blit(ball.image, ball.rect)
                ball.update()
                if not ball.alive:
                    del balls[i]
        pygame.display.flip()
        clock.tick(65)


if __name__ == "__main__":
    main()
