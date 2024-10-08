import random
from multiprocessing.pool import worker

from pico2d import *

# Game object class here\
class Grass:
    def __init__(self): #생성자를 이용해서 객체의 초기 상태를 정의
        self.image = load_image('grass.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(400, 30)
    pass


class Boy:
    def __init__(self):
        self.x , self.y = random.randint(0, 250), 90
        self.frame = random.randint(0, 7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame +1) %8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
    pass

class Ball:
    def __init__(self):
        self.x, self.y = random.randint(0, 700), random.randint(400, 599)
        self.image = random.randint(1, 2)
        if (self.image == 1):
            self.image = load_image('ball21x21.png')
        else:
            self.image = load_image('ball41x41.png')

    def update(self):
        a = random.randint(1, 10)
        speed = a / 1000
        for i in range(0, 100+1, 4):
            t = i/100
            self.x = (1-t*speed) * self.x + (t*speed) * self.x
            self.y = (1-t*speed) * self.y + (t*speed) * 65

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


def reset_world(): #초기화하는 함수
    global running
    global grass
    global team
    global ball
    global world

    running = True
    world = []

    grass = Grass()
    world.append(grass)

    team = [Boy() for i in range(10)]
    world += team

    ball = [Ball() for i in range(20)]
    world += ball

def update_world():
    for o in world:
       o.update()
    pass


def render_world():
   clear_canvas()
   for o in world:
       o.draw()
   update_canvas()


open_canvas()

# initialization code
reset_world()

# game main loop code
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)

# finalization code

close_canvas()
