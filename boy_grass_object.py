from pico2d import *
import random

# Game object class here
class Grass:
    def __init__(self):
        self.image = load_image("grass.png")
        
    def draw(self):
        self.image.draw(400, 30)
    
    def update(self): pass
    
class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)
        self.image = load_image("run_animation.png")
        
    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5
    
    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

class Big_Ball:
    def __init__(self):
        self.x, self.y = random.randint(0, 800), 599
        self.speed = random.randint(5, 20)
        self.image = load_image("ball41x41.png")
    
    def update(self):
        if (self.y > 50 + 21):
            self.y -= self.speed
        else:
            self.y = 50 + 21
    
    def draw(self):
        self.image.draw(self.x, self.y)

class Small_Ball:
    def __init__(self):
        self.x, self.y = random.randint(0, 800), 599
        self.speed = random.randint(5, 20)
        self.image = load_image("ball21x21.png")
    
    def update(self):
        if (self.y > 50 + 11):
            self.y -= self.speed
        else:
            self.y = 50 + 11
    
    def draw(self):
        self.image.draw(self.x, self.y)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

# initialization code
def reset_world():
    global running
    global grass
    # global boy
    global team
    global world
    global balls
    
    running = True
    world = []
    
    grass = Grass()
    world.append(grass)
    
    # boy = Boy()
    team = [Boy() for i in range(11)]
    world += team
    
    num = random.randint(1, 19)
    balls = [Big_Ball() for i in range(num)]
    for i in range(20 - num):
        balls.append(Small_Ball())
    world += balls

def update_world():
    # grass.update()
    # # boy.update()
    # for boy in team:
    #     boy.update()
    # pass
    
    for o in world:
        o.update()

def render_world():
    clear_canvas()
    # grass.draw()
    # # boy.draw()
    # for boy in team:
    #     boy.draw()
    
    for o in world:
        o.draw()
    update_canvas()

# game main loop code

open_canvas()

reset_world()

while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)

# finalization code

close_canvas()
