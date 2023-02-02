"""Simple example that bounces one ball against a floor.
The BallPhysics class defines the "model".  The Ball class is the "view".

@author: Victor Norman
"""

from tkinter import *

import pygame
import pymunk.pygame_util
import pymunk
from pymunk import Vec2d
import math, sys, random


class Ball:

    RADIUS = 10

    def __init__(self, window):
        self._window = window
        self._window.title("Bouncing Ball with pymunk physics")

        self._model = BallPhysics()

        self._width = 400

        self._canvas = Canvas(self._window, bg='black',
                              width=self._width, height=self._width)
        self._canvas.pack()

        self._render()

    def _render(self):
        print("test")
        # self._model.next_step()


class BallPhysics:
    def __init__(self):
        # pygame.init()
        # SCREEN_WIDTH = 1200
        # SCREEN_HEIGHT = 678
        #
        # #game window
        # self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        # pygame.display.set_caption("Pool")


        #pymunk space
        self.space = pymunk.Space()
        static_body = self.space.static_body
        # self.draw_options = pymunk.pygame_util.DrawOptions(self.screen)


        #clock
        self.clock = pygame.time.Clock()
        self.FPS = 120


        #colours
        self.BG = (50, 50, 50)



        #load images
        self.table_image = pygame.image.load("assets/carromboardimage.jpeg")

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
            self.space.add(body, shape, pivot)
            return shape


        self.new_ball = create_ball(10, (300, 200))


        self.cue_ball = create_ball(15, (300, 300))

        #create pool table cushions
        cushions = [
            [(0,0), (0, 40), (500,40), (500, 0)],
        ]


        #function for creating cushions
        def create_cushion(poly_dims):
            body = pymunk.Body(body_type = pymunk.Body.STATIC)
            body.position = ((0,0))
            shape = pymunk.Poly(body, poly_dims)


            self.space.add(body, shape)


        for c in cushions:
            create_cushion(c)

    def next_step(self):
        self.clock.tick(self.FPS)
        self.space.step(1/ self.FPS)

        #fill bgd
        # self.screen.fill(self.BG)

        #draw pool table
        # self.screen.blit(self.table_image, (0,0))


        #event handler
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.cue_ball.body.apply_impulse_at_local_point((0,-1500), (0,0))
            if event.type == pygame.QUIT:
                run = False

        # self.space.debug_draw(self.draw_options)
        pygame.display.update()


main = Tk()
app = Ball(main)
main.mainloop()