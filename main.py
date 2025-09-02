import sys
import pygame as pg
import random
from button import Button
from config import back_btn
from Algorithms import (
    bubblesort as bs,
    binarysearch as bin_search,
    linearsearch as ls,
    insertionsort as ins,
    selectionsort as slc,
    mergesort as mrg,
)

pg.init()

icon = pg.image.load("icon.png")
pg.display.set_icon(icon)

# -------- Constants --------
WIDTH, HEIGHT = 1024, 576
TITLE_TEXT_COLOR = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 120, 215)
BLUE_HOVER = (0, 100, 180)
RED = (255, 0, 0)
RED_HOVER = (200, 0, 0)

scroll_offset = 0
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


# -------- Globals --------
current_screen = "menu"
values = []


# -------- Functions --------
def show_welcome_screen():
    SCREEN.fill(WHITE)
    splash = pg.image.load("lightmode_logo.png").convert_alpha()
    splash = pg.transform.smoothscale(splash, (600, 600))
    splash_rect = splash.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    SCREEN.blit(splash, splash_rect)
    pg.display.update()
    pg.time.delay(1500)
    SCREEN.fill(WHITE)
    pg.display.update()


def handle_scroll(event, scroll_offset, text_lines, top_offset):
    if event.type == pg.MOUSEBUTTONDOWN:
        if event.button == 4:
            scroll_offset = max(scroll_offset - 20, 0)
        elif event.button == 5:
            max_scroll = max(0, len(text_lines) * 28 - (HEIGHT - top_offset))
            scroll_offset = min(scroll_offset + 20, max_scroll)
    return scroll_offset


def reset_values():
    global values
    step = (max_height - min_height) // NUM_BARS
    values = [min_height + (i * step) for i in range(NUM_BARS)]
    random.shuffle(values)


def handle_back_button_events(event):
    global current_screen, bubble_sort_running
    if event.type == pg.MOUSEBUTTONDOWN:
        if back_btn.rect.collidepoint(event.pos):
            current_screen = "menu"
            bubble_sort_running = False


def draw_menu():
    SCREEN.fill(WHITE)
    title_surface = title_font.render("Algorithms", True, TITLE_TEXT_COLOR)
    title_rect = title_surface.get_rect(center=(WIDTH // 2, 60))
    SCREEN.blit(title_surface, title_rect)

    for btn in buttons:
        btn.draw(SCREEN)


def bubble_sort():
    global current_screen
    current_screen = "bubble sort"
    bs.start_bubble_sort()


def insertion_sort():
    global current_screen
    current_screen = "insertion sort"
    ins.start_insertion_sort()  # Initialize insertion sort variables here


def selection_sort():
    global current_screen
    current_screen = "selection sort"
    slc.start_selection_sort()


def merge_sort():
    global current_screen
    current_screen = "merge sort"
    mrg.start_merge_sort()


def linear_search():
    global current_screen
    current_screen = "linear search"
    ls.start_linear_search()  # Initialize the linear search array and variables


def binary_search():
    global current_screen
    current_screen = "binary search"
    bin_search.start_binary_search()


def quit():
    pg.quit()
    sys.exit()


# -------- Buttons --------
bubble_btn = Button(
    text="Bubble Sort",
    x=(WIDTH - 300) // 2,
    y=150,
    width=300,
    height=50,
    color=BLUE,
    hover_color=BLUE_HOVER,
    action=bubble_sort,
)

insertion_btn = Button(
    text="Insertion Sort",
    x=(WIDTH - 300) // 2,
    y=210,
    width=300,
    height=50,
    color=BLUE,
    hover_color=BLUE_HOVER,
    action=insertion_sort,
)

selection_btn = Button(
    text="Selection Sort",
    x=(WIDTH - 300) // 2,
    y=270,
    width=300,
    height=50,
    color=BLUE,
    hover_color=BLUE_HOVER,
    action=selection_sort,
)

merge_btn = Button(
    text="Merge Sort",
    x=(WIDTH - 300) // 2,
    y=330,
    width=300,
    height=50,
    color=BLUE,
    hover_color=BLUE_HOVER,
    action=merge_sort,
)

linear_btn = Button(
    text="Linear Search",
    x=(WIDTH - 300) // 2,
    y=390,
    width=300,
    height=50,
    color=BLUE,
    hover_color=BLUE_HOVER,
    action=linear_search,
)

binary_btn = Button(
    text="Binary Search",
    x=(WIDTH - 300) // 2,
    y=450,
    width=300,
    height=50,
    color=BLUE,
    hover_color=BLUE_HOVER,
    action=binary_search,
)

quit_btn = Button(
    text="Quit",
    x=(WIDTH - 300) // 2,
    y=510,
    width=300,
    height=50,
    color=RED,
    hover_color=RED_HOVER,
    action=quit,
)

buttons = [
    bubble_btn,
    insertion_btn,
    selection_btn,
    merge_btn,
    linear_btn,
    binary_btn,
    quit_btn,
]

# -------- Main Loop --------
show_welcome_screen()

clock = pg.time.Clock()
running = True
while running:
    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:
            running = False

        # Handle back button clicks on sorting screens
        if current_screen != "menu":
            handle_back_button_events(event)

        # Handle main menu buttons only if on menu
        if current_screen == "menu":
            for btn in buttons:
                btn.handle_event(event)

        # Bubble sort scroll
        if current_screen == "bubble sort":
            bs.scroll_offset = handle_scroll(
                event, bs.scroll_offset, bs.bubble_sort_text, 330
            )

        # Insertion sort scroll
        elif current_screen == "insertion sort":
            ins.insertion_scroll_offset = handle_scroll(
                event, ins.insertion_scroll_offset, ins.insertion_sort_text, 250
            )

        elif current_screen == "selection sort":
            slc.selection_scroll_offset = handle_scroll(
                event, slc.selection_scroll_offset, slc.selection_sort_text, 330
            )

        elif current_screen == "merge sort":
            mrg.merge_scroll_offset = handle_scroll(
                event, mrg.merge_scroll_offset, mrg.merge_sort_text, 330
            )

        elif current_screen == "linear search":
            ls.linear_scroll_offset = handle_scroll(
                event, ls.linear_scroll_offset, ls.linear_search_text, 330
            )

        elif current_screen == "binary search":
            bin_search.binary_scroll_offset = handle_scroll(
                event,
                bin_search.binary_scroll_offset,
                bin_search.binary_search_text,
                330,
            )

    # Screen rendering
    if current_screen == "menu":
        draw_menu()
    else:
        SCREEN.fill(WHITE)
        # Draw title at the top center for every screen except menu
        title_surface = title_font.render(
            current_screen.replace("-", " ").title(), True, TITLE_TEXT_COLOR
        )
        title_rect = title_surface.get_rect(midtop=(WIDTH // 2, 10))
        SCREEN.blit(title_surface, title_rect)

        if current_screen == "bubble sort":
            if bs.bubble_sort_running:
                bs.update_bubble_sort()
            bs.draw_bubble_sort()
        elif current_screen == "insertion sort":
            if ins.insertion_sort_running:
                ins.update_insertion_sort()
            ins.draw_insertion_sort()

        elif current_screen == "selection sort":
            if slc.selection_sort_running:
                slc.update_selection_sort()
            slc.draw_selection_sort()

        elif current_screen == "merge sort":
            if mrg.merge_sort_running:
                mrg.update_merge_sort()
            mrg.draw_merge_sort()

        elif current_screen == "linear search":
            if ls.linear_search_running:
                ls.update_linear_search()
            ls.draw_linear_search()

        elif current_screen == "binary search":
            if bin_search.binary_search_running:
                bin_search.update_binary_search()
            bin_search.draw_binary_search()

        else:
            # Placeholder for other sorting screens
            back_btn.draw(SCREEN)
        back_btn.draw(SCREEN)
    pg.display.update()
    clock.tick(60)

pg.quit()
sys.exit()
