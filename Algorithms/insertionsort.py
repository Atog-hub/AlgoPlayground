import pygame as pg
import config as conf
import random

# Insertion sort variables and text
insertion_i = 1
insertion_j = 0
insertion_key = None
insertion_sort_running = False
insertion_scroll_offset = 0


insertion_sort_text = [
    "Insertion Sort Pseudocode:",
    "",
    "for i from 1 to n-1:",
    "    key = A[i]",
    "    j = i - 1",
    "    while j >= 0 and A[j] > key:",
    "        A[j + 1] = A[j]",
    "        j = j - 1",
    "    A[j + 1] = key",
    "",
    "Explanation:",
    "- Starts from the second element, assuming the first is sorted.",
    "- Picks the 'key' element to insert into the sorted part.",
    "- Shifts elements greater than 'key' one position to the right.",
    "- Inserts the 'key' into its correct position.",
    "- Repeats until the entire list is sorted."
]


def reset_values():
    global values
    step = (conf.max_height - conf.min_height) // conf.NUM_BARS
    values = [conf.min_height + (i * step) for i in range(conf.NUM_BARS)]
    random.shuffle(values)

def start_insertion_sort():
    reset_values()
    global insertion_i, insertion_j, insertion_key, insertion_sort_running, scroll_offset
    insertion_i = 1
    insertion_j = 0
    insertion_key = None
    insertion_sort_running = True  # Changed to True to start animation
    scroll_offset = 0
    insertion_key = values[insertion_i]  # Initialize the key at start
    insertion_j = insertion_i - 1

def update_insertion_sort():
    global insertion_i, insertion_j, insertion_key, insertion_sort_running

    if insertion_i < len(values):
        if insertion_j >= 0 and values[insertion_j] > insertion_key:
            values[insertion_j + 1] = values[insertion_j]
            insertion_j -= 1
        else:
            values[insertion_j + 1] = insertion_key
            insertion_i += 1  # Increment by 1, not by insertion_key
            if insertion_i < len(values):
                insertion_key = values[insertion_i]
                insertion_j = insertion_i - 1
            else:
                insertion_sort_running = False
    else:
        insertion_sort_running = False

def draw_insertion_sort():
    TITLE_HEIGHT = 60
    ANIMATION_HEIGHT = 250
    PSEUDO_START_Y = TITLE_HEIGHT + ANIMATION_HEIGHT + 20
    PSEUDO_AREA_HEIGHT = conf.HEIGHT - PSEUDO_START_Y

    # Draw bars
    animation_width = len(values) * conf.BAR_WIDTH
    left_margin = (conf.WIDTH - animation_width) // 2
    animation_top = 125

    for index, val in enumerate(values):
        color = conf.BLUE
        if insertion_sort_running:
            if index == insertion_i:
                color = (255, 0, 0)  # red for current key
            elif index == insertion_j:
                color = (0, 255,255 )  # orange for comparison
        elif not insertion_sort_running:
            color = (0, 200, 0)  # green when sorted

        x = left_margin + index * conf.BAR_WIDTH
        y = animation_top + ANIMATION_HEIGHT - val
        pg.draw.rect(conf.SCREEN, color, (x, y, conf.BAR_WIDTH, val))

    # Draw pseudocode area
    pseudo_surface = pg.Surface((conf.WIDTH, PSEUDO_AREA_HEIGHT))
    pseudo_surface.fill((240, 240, 240))
    for idx, line in enumerate(insertion_sort_text):
        y = idx * 28 - insertion_scroll_offset
        if 0 <= y < PSEUDO_AREA_HEIGHT:
            rendered = conf.font.render(line, True, (0, 0, 0))
            pseudo_surface.blit(rendered, (20, y))
    conf.SCREEN.blit(pseudo_surface, (0, PSEUDO_START_Y))

    # Draw back button
    conf.back_btn.draw(conf.SCREEN)
