import pymunk.pygame_util
import pygame
import pymunk

# INITIAL CODE
pygame.init()

# set screen width and height
SCREEN_WIDTH = 1366
SCREEN_HEIGHT = 678

# game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Play Carrom!")

# the space
space = pymunk.Space()  # defines the shape in which Pymunk physics is applied
static_body = space.static_body
options = pymunk.pygame_util.DrawOptions(screen)
options.flags = pymunk.SpaceDebugDrawOptions.DRAW_SHAPES  # shows only shapes, not constraints

# clock - defines how often the space is updated
clock = pygame.time.Clock()
FPS = 120  # screen is updated 120 times per second

# colours
BG = (50, 50, 50)  # background colour of screen

# define properties of coins and create an array
coin = []  # creates an array with all coins included
# properties : is a tuple in the format (xcoord, ycoord, colour)
properties = ((337, 300, "white"), (337, 320, "black"), (337, 340, "red"), (337, 360, "white"),
              (337, 380, "white"), (318, 310, "black"), (318, 330, "white"), (318, 350, "black"),
              (318, 370, "black"), (300, 320, "white"), (300, 341, "black"), (300, 361, "white"),
              (355, 309, "black"), (355, 329, "white"), (355, 349, "black"), (355, 369, "black"),
              (372, 320, "white"), (372, 340, "black"), (372, 360, "white"))

# dimensions of edges
edges = []  # array including all edges with positions as (x,y)
edges_dimens = [
    [(65, 75), (65, 120), (608, 75), (608, 120)],  # top edge
    [(65, 565), (65, 605), (608, 565), (608, 605)],  # bottom edge
    [(65, 120), (110, 120), (65, 565), (110, 565)],  # lefthand edge
    [(563, 120), (563, 565), (608, 120), (608, 565)]  # righthand edge
]

# dimensions of position slider
slider_position_dimensions = (805, 75), (805, 120), (1348, 75), (1348, 120)
slider_position_bar_dimensions = (805, 55), (805, 140), (815, 55), (815, 140)

# dimensions of force slider
slider_force_dimensions = (805, 175), (805, 220), (1348, 175), (1348, 220)
slider_force_bar_dimensions = (805, 155), (805, 240), (815, 155), (815, 240)

bar_dimensions = (805, 55), (805, 140), (815, 55), (815, 140)
bar_dimensions2 = (805, 155), (805, 240), (815, 155), (815, 240)

# button dimensions
button_dimensions = (805, 255), (805, 340), (905, 255), (905, 340)

global xglobal
xglobal = 805


def convert_coordinates(point):
    return int(point[0]), 678 - int(point[1])


class Coin:
    def __init__(self, x, y, coin_radius, colour):
        self.body = pymunk.Body()  # defines the coin as a pymunk body
        self.body.position = x, y  # takes in x,y coords to position the body on the screen
        self.coin_radius = coin_radius  # takes in argument coin_radius to set the size of the coin
        self.shape = pymunk.Circle(self.body, coin_radius)  # sets the shape of the coin as a circle
        if colour == "red":
            self.shape.color = (255, 80, 100, 255)  # makes the coin red
        elif colour == "white":
            self.shape.color = (255, 255, 255, 255)  # makes the coin white
        elif colour == "black":
            self.shape.color = (0, 0, 0, 0)  # makes the coin black
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

    def changePos(self, slider, y):
        x =  (194 + (((slider.current_dimensions.central_value - 805) / 543) * 283))
        self.x1 = x
        self.y1 = y
        self.body.position = x, y

    def moveStriker(self, forcer):
        force = -1 * (((forcer.current_dimensions.central_value - 805) / 543) * 283)*100
        self.body.apply_impulse_at_local_point((0, force), (0, 0))


class Board:
    def __init__(self):
        self.table_image = pygame.image.load(
            "/Users/ashri/git/carrom-board/src/assets/nusry-n-0RIEyCTxz4I-unsplash.jpg").convert_alpha()
        #  load image
        self.table_imagereal = pygame.transform.scale(self.table_image, (678, 678))
        #  scales image to board size

    def draw(self):
        screen.blit(self.table_imagereal, (0, 0))
        # draws carrom board on the screen


class Edges:
    def __init__(self, dimens):
        self.body = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.body.position = ((0, 0))
        self.shape = pymunk.Poly(self.body, dimens)
        self.shape.elasticity = 0.8

    def draw(self):
        space.add(self.body, self.shape)



class GameDimension: # This is utility class used for getting the multiple properties
    def __init__(self, slidebar_dimensions, central_value):
        self.slidebar_dimensions = slidebar_dimensions
        self.central_value = central_value


class Button:
    def __init__(self, dimens):
        self.body = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.body.position = ((0, 0))
        self.shape = pymunk.Poly(self.body, dimens)
        space.add(self.body, self.shape)

    def CheckClicked(self, initial_dimensions):
        mouse_pos = pygame.mouse.get_pos()
        if initial_dimensions[0][0] < mouse_pos[0] < initial_dimensions[2][0] and initial_dimensions[1][1] > mouse_pos[
            1] > initial_dimensions[2][1]:
            return ('True')
        else:
            return ('False')

class Slider:
    def __init__(self, dimensions_base, dimensions_bar):
        self.initial_dimensions = dimensions_base
        self.slide_base = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.slide_base.position = ((0, 0))
        self.slide_bar_holder_shape = pymunk.Poly(self.slide_base, self.initial_dimensions)
        space.add(self.slide_base, self.slide_bar_holder_shape)

        self.slide_bar = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.initial_bar_dimensions = dimensions_bar
        self.slide_bar.position = ((0, 0))
        self.current_dimensions = self.get_dimensions()
        self.dimens_bar = self.current_dimensions.slidebar_dimensions
        self.slide_bar_shape = pymunk.Poly(self.slide_bar, self.dimens_bar)
        self.slide_bar_shape.color = (255, 80, 100, 255)
        space.add(self.slide_bar, self.slide_bar_shape)

    def move(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.initial_dimensions[0][0] < mouse_pos[0] < self.initial_dimensions[2][0] \
                and self.initial_dimensions[1][1] > mouse_pos[1] > self.initial_dimensions[2][1]:
            space.remove(self.slide_bar, self.slide_bar_shape)
            self.dimens_bar = self.get_dimensions().slidebar_dimensions
            self.slide_bar_shape = pymunk.Poly(self.slide_bar, self.dimens_bar)
            self.slide_bar_shape.color = (255, 80, 100, 255)
            space.add(self.slide_bar, self.slide_bar_shape)

    def get_dimensions(self):
        mouse_pos = pygame.mouse.get_pos()
        striker_position = mouse_pos[0]
        y = (self.initial_dimensions[0][1] + self.initial_dimensions[1][1]) / 2
        x = mouse_pos[0]
        avgx = (self.initial_bar_dimensions[2][0] - self.initial_bar_dimensions[0][0]) / 2
        avgy = (self.initial_bar_dimensions[1][1] - self.initial_bar_dimensions[0][1]) / 2
        slider_bar_dimens = (x - avgx, y + avgy), (x - avgx, y - avgy), (x + avgx, y + avgy), (x + avgx, y - avgy)
        if self.initial_dimensions == ((805, 75), (805, 120), (1348, 75), (1348, 120)):
            global bar_dimensions
            bar_dimensions = slider_bar_dimens
        else:
            global bar_dimensions2
            bar_dimensions2 = slider_bar_dimens

        self.current_dimensions = GameDimension(slider_bar_dimens, striker_position)
        return self.current_dimensions


def game():
    for x in range(19):
        coin.append(Coin(properties[x][0], properties[x][1], 10, properties[x][2]))
        # creates 19 coins with the properties in the tuple listed above
        coin[x].draw()  # draws coins on the board

    global xglobal
    StrikerCoin = Coin(xglobal, 590, 15, "white")
    StrikerCoin.draw()

    # the edges
    for e in edges_dimens:
        edges.append(Edges(e))
    for i in range(4):
        edges[i].draw()

    slider = Slider(slider_position_dimensions, slider_position_bar_dimensions)
    forcer = Slider(slider_force_dimensions, slider_force_bar_dimensions)
    Gobutton = Button(button_dimensions)

    while True:
        clock.tick(FPS)  # defines how often the space updates
        space.step(1 / FPS)  # space-time moved in steps using this function
        # fill bgd
        screen.fill(BG)
        # event handler
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                slider.move()
                forcer.move()
                StrikerCoin.changePos(slider,  490)
                if Gobutton.CheckClicked(button_dimensions) == ('True'):
                    StrikerCoin.moveStriker(forcer)

            if event.type == pygame.QUIT:
                return
        board = Board()
        board.draw()
        space.debug_draw(options)
        pygame.display.update()


game()
pygame.quit()
