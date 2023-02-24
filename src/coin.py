
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
        self.x1 = x
        self.y1 = y
        self.body.position = x, y

    def moveStriker(self):
        self.body.apply_impulse_at_local_point((500, -300), (0,0))
