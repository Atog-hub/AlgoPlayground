import pygame as pg
import random
from config import SCREEN, WHITE, HEIGHT, WIDTH, BAR_WIDTH, title_font, TITLE_TEXT_COLOR, BLUE, font, back_btn

#Linear search variable and text
linear_num_bars = 50
linear_scroll_offset = 0
linear_search_running = False
linear_found_index = -1
linear_current_index = 0
linear_bar_width = 0  # will set in draw function or start function


linear_array = []
linear_num_bars = 50
linear_bar_width = WIDTH // linear_num_bars
linear_target = None
linear_current_index = 0
linear_search_running = False
linear_found_index = -1
linear_scroll_offset = 0

linear_search_text = [
        "Linear Search Pseudocode:",
        "",
        "for i from 0 to n-1:",
        "    if array[i] == target:",
        "        return i",
        "return -1",
        "",
        "Explanation:",
        "- Iterate through the list one by one.",
        "- Compare each element with the target value.",
        "- Stop when the target is found or end is reached.",
    ]



def start_linear_search():
    global linear_array, linear_target, linear_current_index, linear_search_running, linear_found_index

    min_val = 50
    max_val = 400
    step = (max_val - min_val) // linear_num_bars
    linear_array = [min_val + i * step for i in range(linear_num_bars)]
    random.shuffle(linear_array)

    linear_target = random.choice(linear_array)
    linear_current_index = 0
    linear_search_running = True
    linear_found_index = -1

def update_linear_search():
    global linear_current_index, linear_search_running, linear_found_index

    if linear_search_running:
        if linear_current_index < len(linear_array):
            if linear_array[linear_current_index] == linear_target:
                linear_found_index = linear_current_index
                linear_search_running = False
            else:
                linear_current_index += 1
        else:
            linear_search_running = False

def draw_linear_search():
    global linear_scroll_offset
    global linear_bar_width  # so we can calculate it dynamically

    TITLE_HEIGHT = 60
    ANIMATION_HEIGHT = 250
    PSEUDO_START_Y = TITLE_HEIGHT + ANIMATION_HEIGHT + 20
    PSEUDO_AREA_HEIGHT = HEIGHT - PSEUDO_START_Y

    SCREEN.fill(WHITE)

    title_surface = title_font.render("Linear Search", True, TITLE_TEXT_COLOR)
    SCREEN.blit(title_surface, (WIDTH // 2 - title_surface.get_width() // 2, 10))

    padding = 100
    available_width = WIDTH - 2 * padding
    linear_bar_width = available_width // linear_num_bars
    left_margin = padding
    animation_top = 100

    max_val = max(linear_array) if linear_array else 1
    for idx, val in enumerate(linear_array):
        bar_height = int(val / max_val * ANIMATION_HEIGHT)
        x = left_margin + idx * linear_bar_width
        y = animation_top + ANIMATION_HEIGHT - bar_height

        color = BLUE
        if idx == linear_current_index and linear_search_running:
            color = (255, 165, 0)  # orange for current check
        elif idx == linear_found_index:
            color = (0, 255, 0)  # green if found
        pg.draw.rect(SCREEN, color, (x, y, linear_bar_width - 2, bar_height))

    # Show target value
    target_text = font.render(f"Target Value: {linear_target}", True, (0, 0, 0))
    SCREEN.blit(target_text, (10, TITLE_HEIGHT))

    # Draw pseudocode area
    pseudo_surface = pg.Surface((WIDTH, PSEUDO_AREA_HEIGHT))
    pseudo_surface.fill((240, 240, 240))

    line_height = 28
    for idx, line in enumerate(linear_search_text):
        y = idx * line_height - linear_scroll_offset
        if -line_height < y < PSEUDO_AREA_HEIGHT:
            rendered = font.render(line, True, (0, 0, 0))
            pseudo_surface.blit(rendered, (20, y))

    SCREEN.blit(pseudo_surface, (0, PSEUDO_START_Y))

    # Draw back button
    back_btn.draw(SCREEN)