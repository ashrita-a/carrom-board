import pymunk.pygame_util
import pygame
import pymunk
import tkinter
"""" import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button """

pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 678


#game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pool")


#pymunk space
space = pymunk.Space()
static_body = space.static_body
draw_options = pymunk.pygame_util.DrawOptions(screen)


#clock
clock = pygame.time.Clock()
FPS = 120


#colours
BG = (50, 50, 50)



#load images
table_image = pygame.image.load("assets/carromboardimage.jpeg").convert_alpha()

#function for creating balls
def create_ball(radius, pos):
    body = pymunk.Body()
    body.position = pos
    shape = pymunk.Circle(body, radius)
    shape.mass = 5
    #use pivot joint for friction
    pivot = pymunk.PivotJoint(static_body, body, (0,0), (0,0))
    pivot.max_bias = 0 #disable joint correction
    pivot.max_force = 1000 #emulate linear friction
    space.add(body, shape, pivot)
    return shape


new_ball = create_ball(10, (300, 200))


cue_ball = create_ball(15, (300, 300))

# #drawing slider
# def create_Slider(rangevalues):
#     slider1 = pygame.widgets.RangeSlider(range_values= rangevalues)
#     space.add(slider1)
#     return slider1
#
# slider_horiz = create_Slider(69)


#create pool table cushions
cushions = [
    [(0,0), (0, 40), (500,40), (1000, 0)], [(100,0), (100, 40), (600,40), (600, 0)]
]


#function for creating cushions
def create_cushion(poly_dims):
    body = pymunk.Body(body_type = pymunk.Body.STATIC)
    body.position = ((0,0))
    shape = pymunk.Poly(body, poly_dims)
    space.add(body, shape)


for c in cushions:
    create_cushion(c)


#game loop
run = True
while run:

    clock.tick(FPS)
    space.step(1/ FPS)

    #fill bgd
    screen.fill(BG)

    #draw pool table
    screen.blit(table_image, (0,0))


    #event handler
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            cue_ball.body.apply_impulse_at_local_point((0,-1500), (0,0))
        if event.type == pygame.QUIT:
            run = False

    space.debug_draw(draw_options)
    pygame.display.update()


pygame.quit()
