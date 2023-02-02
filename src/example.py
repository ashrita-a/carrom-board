"""Simple example that bounces one ball against a floor.
The BallPhysics class defines the "model".  The Ball class is the "view".

@author: Victor Norman
"""

from tkinter import *
import pymunk
import pymunk.util
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

        self._model.next_step()
        x, y = self._model.get_xy_for_ball()

        # subtract y values from self._width because y increases from 0 downward.
        self._canvas.create_oval(x - self.RADIUS, self._width - (y - self.RADIUS),
                                 x + self.RADIUS, self._width - (y + self.RADIUS),
                                 fill = 'white')
        self._canvas.after(20, self._render)


class BallPhysics:
    def __init__(self):

        self._space = pymunk.Space()
        self._space.gravity = (0.0, -900.0)

        self._balls = []

        mass = 10
        inertia = pymunk.moment_for_circle(mass, 0, Ball.RADIUS, (0, 0))
        body = pymunk.Body(mass, inertia)
        x = random.randint(50, 350)
        body.position = x, 400
        shape = pymunk.Circle(body, Ball.RADIUS, Vec2d(0,0))
        shape.elasticity = 0.9
        self._space.add(body, shape)
        self._balls.append(shape)

        # floor
        floor = pymunk.Segment(self._space.static_body, (0.0, 10.0), (400.0, 10.0), 1.0)
        floor.friction = 1.0
        floor.elasticity = 0.9
        self._space.add(floor)


    def next_step(self):
        # Remove balls that are below the bottom.
        balls_to_remove = []
        for ball in self._balls:
            if ball.body.position.y < 0:
                balls_to_remove.append(ball)
        for ball in balls_to_remove:
            self._space.remove(ball, ball.body)
            self._balls.remove(ball)

        if len(self._balls) >= 1:
            v = self._balls[0].body.position
            print("point = %.2f, %.2f" % (v.x, v.y))

        self._space.step(1 / 50)

    def get_xy_for_ball(self):
        ball_num = 0
        return (self._balls[ball_num].body.position.x,
                self._balls[ball_num].body.position.y)


main = Tk()
app = Ball(main)
main.mainloop()