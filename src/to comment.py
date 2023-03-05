

# DATE: 25TH FEB
# WHAT I DID: I MADE THE CIRCULAR SLIDER STUFF

class Circular_Slider:
    def __init__(self, base_radius, position_circle_base, position_circle_slide, circle_slide_radius):
        self.circle_base_position = position_circle_base
        self.circle_slide_base = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.circle_slide_base.position = ((self.circle_base_position[0], self.circle_base_position[1]))
        self.base_radius = base_radius
        self.slide_bar_holder_shape = pymunk.Circle(self.circle_slide_base, base_radius)
        space.add(self.circle_slide_base, self.slide_bar_holder_shape)

        self.circle_bar_position = position_circle_slide
        self.circle_slide = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.posit_circle_slide = self.get_position()
        self.circle_slide.position = ((self.posit_circle_slide[0], self.posit_circle_slide[1]))
        self.circle_slide_radius = circle_slide_radius
        self.circle_slide_shape = pymunk.Circle(self.circle_slide, self.circle_slide_radius)
        self.circle_slide_shape.color = (255, 80, 100, 255)
        space.add(self.circle_slide, self.circle_slide_shape)

    def move(self):
        mouse_pos = pygame.mouse.get_pos()
        x1 = self.circle_base_position[0]
        y1 = self.circle_base_position[1]
        x = mouse_pos[0] - x1
        y = mouse_pos[1] - y1
        if math.pow(x,2) + math.pow(y,2) < math.pow(self.base_radius, 2) or math.pow(x,2) + math.pow(y,2) == math.pow(self.base_radius, 2) :
            space.remove(self.circle_slide, self.circle_slide_shape)
            self.posit_circle_slide = self.get_position()
            self.circle_slide.position = ((self.posit_circle_slide[0], self.posit_circle_slide[1]))
            self.circle_slide_shape = pymunk.Circle(self.circle_slide, self.circle_slide_radius)
            self.circle_slide_shape.color = (255, 80, 100, 255)
            space.add(self.circle_slide, self.circle_slide_shape)


    def get_position(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_x = mouse_pos[0]
        mouse_y = mouse_pos[1]
        x1 = self.circle_base_position[0]
        y1 = self.circle_base_position[1]
        angle = math.atan((mouse_y - y1 ) / (mouse_x - x1))
        self.xpos = self.base_radius*math.cos(angle) + x1
        self.ypos = self.base_radius*math.sin(angle) + y1
        circle_slide_position = (self.xpos, self.ypos)
        return(circle_slide_position)


the game function:

while True:
    clock.tick(FPS)  # defines how often the space updates
    space.step(1 / FPS)  # space-time moved in steps using this function
    # fill bgd
    screen.fill(BG)
    # event handler
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            sliderpos.move()
            sliderforce.move()
            directionslider.move()
            StrikerCoin.changePos(sliderpos,  490)
            if Gobutton.CheckClicked(button_dimensions) == ('True'):
                StrikerCoin.moveStriker(sliderforce)

        if event.type == pygame.QUIT:
            return




CHANGES MADE:

def get_position(self):
    mouse_pos = pygame.mouse.get_pos()
    mouse_x = mouse_pos[0]
    mouse_y = mouse_pos[1]
    x1 = self.circle_base_position[0]
    y1 = self.circle_base_position[1]
    angle = abs(math.atan((mouse_y - y1 ) / (mouse_x - x1)))
    if mouse_x - x1 < 0:
        self.xpos =  x1 - self.base_radius*math.cos(angle)
    else :
        self.xpos = self.base_radius*math.cos(angle) + x1
    if mouse_y - y1 < 0:
        self.ypos = y1 - self.base_radius*math.sin(angle)
    else:
        self.ypos = y1 + self.base_radius*math.sin(angle)
    circle_slide_position = (self.xpos, self.ypos)
    return(circle_slide_position)



I CHANGED THE SLIDER SO IT LOOKS A BIT COOLER:
class Circular_Slider:
    def __init__(self, base_radius, position_circle_base, position_circle_slide, circle_slide_radius):
        self.circle_base_position = position_circle_base
        self.circle_slide_base = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.circle_slide_base.position = ((self.circle_base_position[0], self.circle_base_position[1]))
        self.base_radius = base_radius
        self.slide_bar_holder_shape = pymunk.Circle(self.circle_slide_base, base_radius)
        space.add(self.circle_slide_base, self.slide_bar_holder_shape)

        self.circle_base_position = position_circle_base
        self.circle_slide_base2 = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.circle_slide_base2.position = ((self.circle_base_position[0], self.circle_base_position[1]))
        self.base_radius2 = base_radius - 8
        self.slide_bar_holder_shape2 = pymunk.Circle(self.circle_slide_base2, self.base_radius2)
        self.slide_bar_holder_shape2.color = (50, 50, 50, 50)
        space.add(self.circle_slide_base2, self.slide_bar_holder_shape2)

        self.circle_bar_position = position_circle_slide
        self.circle_slide = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.posit_circle_slide = self.get_position()
        self.circle_slide.position = ((self.posit_circle_slide[0], self.posit_circle_slide[1]))
        self.circle_slide_radius = circle_slide_radius
        self.circle_slide_shape = pymunk.Circle(self.circle_slide, self.circle_slide_radius)
        self.circle_slide_shape.color = (255, 80, 100, 255)
        space.add(self.circle_slide, self.circle_slide_shape)

    def move(self):
        mouse_pos = pygame.mouse.get_pos()
        x1 = self.circle_base_position[0]
        y1 = self.circle_base_position[1]
        x = mouse_pos[0] - x1
        y = mouse_pos[1] - y1
        if math.pow(x,2) + math.pow(y,2) < math.pow(self.base_radius, 2) or math.pow(x,2) + math.pow(y,2) == math.pow(self.base_radius, 2) :
            space.remove(self.circle_slide, self.circle_slide_shape)
            self.posit_circle_slide = self.get_position()
            self.circle_slide.position = ((self.posit_circle_slide[0], self.posit_circle_slide[1]))
            self.circle_slide_shape = pymunk.Circle(self.circle_slide, self.circle_slide_radius)
            self.circle_slide_shape.color = (255, 80, 100, 255)
            space.add(self.circle_slide, self.circle_slide_shape)


    def get_position(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_x = mouse_pos[0]
        mouse_y = mouse_pos[1]
        x1 = self.circle_base_position[0]
        y1 = self.circle_base_position[1]
        angle = abs(math.atan((mouse_y - y1 ) / (mouse_x - x1)))
        if mouse_x - x1 < 0:
            self.xpos =  x1 - self.base_radius*math.cos(angle)
        else :
            self.xpos = self.base_radius*math.cos(angle) + x1
        if mouse_y - y1 < 0:
            self.ypos = y1 - self.base_radius*math.sin(angle)
        else:
            self.ypos = y1 + self.base_radius*math.sin(angle)
        circle_slide_position = (self.xpos, self.ypos)
        return(circle_slide_position)


