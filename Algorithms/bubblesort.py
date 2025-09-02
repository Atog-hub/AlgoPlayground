import pygame as pg
from config import SCREEN, WHITE, HEIGHT, WIDTH, BAR_WIDTH, title_font, TITLE_TEXT_COLOR, BLUE, font, reset_values, \
    back_btn, max_height, min_height , NUM_BARS
import random

pg.init()
bubble_i = 0
bubble_j = 0
bubble_sort_running = False
scroll_offset = 0

step = (max_height - min_height) // NUM_BARS
values = [min_height + (i * step) for i in range(NUM_BARS)]
random.shuffle(values)

bubble_sort_text = [
    "Bubble Sort Pseudocode:",
    "",
    "for i from 0 to n-1:",
    "    for j from 0 to n-i-1:",
    "        if array[j] > array[j+1]:",
    "            swap array[j] and array[j+1]",
    "",
    "Explanation:",
    "- Repeatedly steps through the list,",
    "- Compares adjacent elements and swaps them if they're in the wrong order.",
    "- Continues until the list is sorted.",
]


def bubble_sort_button_action():
    global current_screen
    current_screen = "bubble sort"
    start_bubble_sort()

def start_bubble_sort():
    global bubble_i, bubble_j, bubble_sort_running, scroll_offset, values
    reset_values()
    bubble_i = 0
    bubble_j = 0
    bubble_sort_running = True
    scroll_offset = 0

    step = (max_height - min_height) // NUM_BARS
    values = [min_height + (i * step) for i in range(NUM_BARS)]
    random.shuffle(values)


def update_bubble_sort():
    global bubble_i, bubble_j, bubble_sort_running

    n = len(values)
    if bubble_i < n:
        if bubble_j < n - bubble_i - 1:
            if values[bubble_j] > values[bubble_j + 1]:
                values[bubble_j], values[bubble_j + 1] = values[bubble_j + 1], values[bubble_j]
            bubble_j += 1
        else:
            bubble_j = 0
            bubble_i += 1
    else:
        bubble_sort_running = False

def draw_bubble_sort():
    global scroll_offset
    SCREEN.fill(WHITE)

    TITLE_HEIGHT = 60
    ANIMATION_HEIGHT = 250
    PSEUDO_START_Y = TITLE_HEIGHT + ANIMATION_HEIGHT + 20
    PSEUDO_AREA_HEIGHT = HEIGHT - PSEUDO_START_Y

    # Draw title
    title_surface = title_font.render("Bubble Sort", True, TITLE_TEXT_COLOR)
    SCREEN.blit(title_surface, title_surface.get_rect(center=(WIDTH // 2, TITLE_HEIGHT // 2)))

    # Draw bars animation
    animation_width = len(values) * BAR_WIDTH
    left_margin = (WIDTH - animation_width) // 2
    animation_top = 125

    for index, val in enumerate(values):
        color = BLUE
        # Highlight bars currently being compared
        if bubble_sort_running and (index == bubble_j or index == bubble_j + 1):
            color = (255, 100, 100)
        elif not bubble_sort_running:
            color = (0, 200, 0)  # Green when sorted
        x = left_margin + index * BAR_WIDTH
        y = animation_top + ANIMATION_HEIGHT - val
        pg.draw.rect(SCREEN, color, (x, y, BAR_WIDTH, val))

    # Draw pseudocode area
    pseudo_surface = pg.Surface((WIDTH, PSEUDO_AREA_HEIGHT))
    pseudo_surface.fill((240, 240, 240))
    for idx, line in enumerate(bubble_sort_text):
        y = idx * 28 - scroll_offset
        if 0 <= y < PSEUDO_AREA_HEIGHT:
            rendered = font.render(line, True, (0, 0, 0))
            pseudo_surface.blit(rendered, (20, y))
    SCREEN.blit(pseudo_surface, (0, PSEUDO_START_Y))

    # Draw back button
    back_btn.draw(SCREEN)
