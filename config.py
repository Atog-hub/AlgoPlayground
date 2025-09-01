import pygame as pg
import random
from button import Button

# -------- Constants --------
WIDTH, HEIGHT = 1024, 576
TITLE_TEXT_COLOR = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 120, 215)
BLUE_HOVER = (0, 100, 180)
RED = (255, 0, 0)
RED_HOVER = (200, 0, 0)


NUM_BARS = 50
min_height = 50
max_height = int(HEIGHT * 0.6)
BAR_WIDTH = HEIGHT // NUM_BARS
PSEUDO_TOP_OFFSET = 60 + 250 + 20

# -------- Setup --------
SCREEN = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("AlgoPlayground")

title_font = pg.font.SysFont("Arial", 50)
font = pg.font.SysFont("Arial", 24)

back_btn = Button(
    text="←",
    x=10,
    y=10,
    width=50,
    height=50,
    color=BLUE,
    hover_color=BLUE_HOVER,
    action=None,
)


def reset_values():
    global values
    step = (max_height - min_height) // NUM_BARS
    values = [min_height + (i * step) for i in range(NUM_BARS)]
    random.shuffle(values)