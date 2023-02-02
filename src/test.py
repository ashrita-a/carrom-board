import pymunk.pygame_util
import pygame
import pymunk
import tkinter

pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 678

# game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pool")

# pymunk space
space = pymunk.Space()
static_body = space.static_body
draw_options = pymunk.pygame_util.DrawOptions(screen)

# clock
clock = pygame.time.Clock()
FPS = 120

# colours
BG = (50, 50, 50)


def convert_coordinates(point):
    return int(point[0]), 600 - int(point[1])


class Coin:
    def __init__(self, x, y, coin_radius):
        self.body = pymunk.Body()  # defines the coin as a pymunk body
        self.body.position = x, y  # takes in x,y coords to position the body on the screen
        self.coin_radius = coin_radius  # takes in argument coin_radius to set the size of the coin
        self.shape = pymunk.Circle(self.body, coin_radius)  # sets the shape of the coin as a circle
        self.shape.mass = 5  # unitless mass for coin
        self.pivot = pymunk.PivotJoint(static_body, self.body, (0, 0), (0, 0))  # using pivot joint for friction
        self.pivot.max_bias = 0  # disables joint correction
        self.pivot.max_force = 1000  # emulates linear friction
        space.add(self.body, self.shape, self.pivot)  # adds the coin to the screen

    def draw(self):
        pygame.draw.circle(screen, (0, 255, 0, 255), convert_coordinates(self.body.position), self.coin_radius)
            #  to draw the coin on the screen

class Board():
    def __init__(self):
        self.table_image = pygame.image.load("/Users/ashri/git/carrom-board/src/assets/nusry-n-0RIEyCTxz4I-unsplash.jpg").convert_alpha()
            #  load image
        self.table_imagereal = pygame.transform.scale(self.table_image, (678,678) )
            #  scales image to board size
    def draw(self):
        screen.blit(self.table_imagereal, (0,0))
            # draws carrom board on the screen




def game():
    # coin = []
    # for x in range(9):
    #     coin.append(Coin(400, 300, 10))
    #     coin[x].draw()
    # StrikerCoin = Coin(100,500,30)

    coin1 = Coin(337, 307, 10)
    coin2 = Coin(337, 327, 10)
    coin1.draw()

    while True:
        clock.tick(FPS)
        space.step(1 / FPS)
        # fill bgd
        screen.fill(BG)
        # event handler
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                StrikerCoin.body.apply_impulse_at_local_point((0, -1500), (0, 0))
            if event.type == pygame.QUIT:
                return
        board = Board()
        board.draw()
        space.debug_draw(draw_options)
        pygame.display.update()


game()
pygame.quit()
