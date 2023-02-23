import pymunk.pygame_util
import pygame
import pymunk
import tkinter
from tkinter import *
import os

#INITIAL CODE
pygame.init()

#set screen width and height
SCREEN_WIDTH = 1366
SCREEN_HEIGHT = 678

# game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Play Carrom!")

# the space
space = pymunk.Space() #defines the shape in which Pymunk physics is applied
static_body = space.static_body
options = pymunk.pygame_util.DrawOptions(screen)
options.flags = pymunk.SpaceDebugDrawOptions.DRAW_SHAPES #shows only shapes, not constraints

# clock - defines how often the space is updated
clock = pygame.time.Clock()
FPS = 120 # screen is updated 120 times per second

# colours
BG = (50, 50, 50) #background colour of screen

#define properties of coins and create an array
coin = [] #creates an array with all coins included
# properties : is a tuple in the format (xcoord, ycoord, colour)
properties = ((337, 300, "white"), (337, 320, "black"), (337, 340, "red"), (337, 360, "white"),
              (337, 380, "white"), (318, 310, "black"), (318, 330, "white"), (318, 350, "black"),
              (318, 370, "black"), (300, 320, "white"), (300, 341, "black"), (300, 361, "white"),
              (355, 309, "black"), (355, 329, "white"), (355, 349, "black"), (355, 369, "black"),
              (372, 320, "white"), (372, 340, "black"), (372, 360, "white"))

# dimensions of edges
edges = [] #array including all edges with positions as (x,y)
edges_dimens = [
    [(65,75), (65, 120), (608,75), (608, 120)], #top edge
    [(65,565), (65, 605), (608,565), (608, 605)], #bottom edge
    [(65,120), (110, 120), (65, 565), (110, 565)], #lefthand edge
    [(563,120), (563,565), (608, 120), (608, 565) ] #righthand edge
]

#dimensions of slider base
sliderbase_dimens = (805,75), (805, 120), (1348,75), (1348, 120)

#dimensions of slider bar
sliderbar_dimens1 = (805,55), (805, 140), (815,55), (815, 140)


def convert_coordinates(point):
    return int(point[0]), 678 - int(point[1])


class Coin:
    def __init__(self, x, y, coin_radius, colour):
        self.body = pymunk.Body()  # defines the coin as a pymunk body
        self.body.position = x, y  # takes in x,y coords to position the body on the screen
        self.coin_radius = coin_radius  # takes in argument coin_radius to set the size of the coin
        self.shape = pymunk.Circle(self.body, coin_radius)  # sets the shape of the coin as a circle
        if colour == "red" :
            self.shape.color = (255, 80, 100, 255) # makes the coin red
        elif colour == "white":
            self.shape.color = (255, 255, 255, 255) # makes the coin white
        elif colour == "black":
            self.shape.color = (0, 0, 0, 0) # makes the coin black
        self.shape.mass = 5  # unitless mass for coin
        self.pivot = pymunk.PivotJoint(static_body, self.body, (0, 0), (0, 0))  # using pivot joint for friction
        self.pivot.max_bias = 0  # disables joint correction
        self.pivot.max_force = 800  # emulates linear friction
        self.shape.elasticity = 0.8
        space.add(self.body, self.shape, self.pivot)  # adds the coin to the screen

    def draw(self):
        x, y = convert_coordinates(self.body.position)
        pygame.draw.circle(screen, self.shape.color, convert_coordinates(self.body.position), self.coin_radius)
                #  to draw the coin on the screen
    def changePos(self, x, y):
        self.body.position = x, y


class Board():
    def __init__(self):
        self.table_image = pygame.image.load("/Users/ashri/git/carrom-board/src/assets/nusry-n-0RIEyCTxz4I-unsplash.jpg").convert_alpha()
            #  load image
        self.table_imagereal = pygame.transform.scale(self.table_image, (678,678) )
            #  scales image to board size
    def draw(self):
        screen.blit(self.table_imagereal, (0,0))
            # draws carrom board on the screen



class Edges():
    def __init__(self, dimens):
        self.body = pymunk.Body(body_type = pymunk.Body.STATIC)
        self.body.position = ((0,0))
        self.shape = pymunk.Poly(self.body, dimens)
        self.shape.elasticity = 0.8
    def draw(self):
        space.add(self.body, self.shape)



class SliderBase():
    def __init__(self, dimens):
        self.body = pymunk.Body(body_type = pymunk.Body.STATIC)
        self.body.position = ((0,0))
        self.shape = pymunk.Poly(self.body, dimens)
    def draw(self):
        space.add(self.body, self.shape)

def GetDimens(lowerlim, upperlim, fixedy,  ):
    mouse_pos = pygame.mouse.get_pos()
    if 805 < mouse_pos[0] < 1348 and 120 > mouse_pos[1] > 75:
        central = mouse_pos[0]
        y = 97.5
        x = mouse_pos[0]
        sliderbar_dimens = (x-5, y+42.5), (x-5, y-42.5), (x+5,y+42.5), (x+5, y-42.5)
    else :
        sliderbar_dimens = sliderbar_dimens1
        central = 805
    return(sliderbar_dimens)

class SliderBar():
    def __init__(self):
        self.body = pymunk.Body(body_type = pymunk.Body.STATIC)
        self.body.position = ((0,0))
        self.dimens_bar = GetDimens()
        self.shape = pymunk.Poly(self.body, self.dimens_bar)
        self.shape.color = (255, 80, 100, 255)

    def draw(self):
        space.add(self.body, self.shape)

    def move(self):
        space.remove(self.body, self.shape)
        self.dimens_bar = GetDimens()
        self.shape = pymunk.Poly(self.body, self.dimens_bar)
        self.shape.color = (255, 80, 100, 255)
        space.add(self.body, self.shape)


def game():
    for x in range(19):
        coin.append(Coin(properties[x][0], properties[x][1], 10, properties[x][2]))
            #creates 19 coins with the properties in the tuple listed above
        coin[x].draw() #draws coins on the board

    StrikerCoin = Coin(318,500,15, "white")
    StrikerCoin.draw()

    # the edges
    for e in edges_dimens:
        edges.append(Edges(e))
    for i in range (4):
        edges[i].draw()

    SliderPos = SliderBase(sliderbase_dimens)
    SliderPos.draw()

    scrollBar = None
    while True:
        clock.tick(FPS) #defines how often the space updates
        space.step(1 / FPS) #space-time moved in steps using this function
        # fill bgd
        screen.fill(BG)
        # event handler
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                StrikerCoin.changePos(194+(((945-805)/543)*283), 490)
                StrikerCoin.body.apply_impulse_at_local_point((0, -30000), (0, 0))
                if scrollBar is not None:
                    scrollBar.move()
                else:
                    scrollBar = SliderBar()
                    scrollBar.draw()

            if event.type == pygame.QUIT:
                return
        board = Board()
        board.draw()
        space.debug_draw(options)
        pygame.display.update()


game()
pygame.quit()
