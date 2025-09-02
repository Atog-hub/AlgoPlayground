import pygame as pg
import random
from config import SCREEN, WHITE, HEIGHT, WIDTH, BAR_WIDTH, title_font, TITLE_TEXT_COLOR, BLUE, font, back_btn

# -------- Globals --------
binary_array = []
binary_target = None
binary_low = 0
binary_high = 0
binary_mid = -1
binary_search_running = False
binary_found_index = -1
binary_scroll_offset = 0
binary_num_bars = 50
binary_bar_width = 0

binary_search_text = [
    "Binary Search Pseudocode:",
    "",
    "low = 0",
    "high = len(array) - 1",
    "while low <= high:",
    "    mid = (low + high) // 2",
    "    if array[mid] == target:",
    "        return mid",
    "    elif array[mid] < target:",
    "        low = mid + 1",
    "    else:",
    "        high = mid - 1",
    "return -1",
    "",
    "Explanation:",
    "- Checks the middle element each iteration.",
    "- Eliminates half the array each time.",
    "- Requires the array to be sorted."
]

def start_binary_search():
    global binary_array, binary_target, binary_low, binary_high, binary_mid
    global binary_search_running, binary_found_index, binary_scroll_offset

    min_val = 50
    max_val = 400
    step = (max_val - min_val) // binary_num_bars

    binary_array = [min_val + i * step for i in range(binary_num_bars)]
    random.shuffle(binary_array)
    binary_array.sort()  # Binary search requires sorted array

    binary_target = random.choice(binary_array)
    binary_low = 0
    binary_high = len(binary_array) - 1
    binary_mid = -1
    binary_found_index = -1
    binary_search_running = True
    binary_scroll_offset = 0


def update_binary_search():
    global binary_low, binary_high, binary_mid, binary_search_running, binary_found_index

    if binary_search_running and binary_low <= binary_high:
        binary_mid = (binary_low + binary_high) // 2
        if binary_array[binary_mid] == binary_target:
            binary_found_index = binary_mid
            binary_search_running = False
        elif binary_array[binary_mid] < binary_target:
            binary_low = binary_mid + 1
        else:
            binary_high = binary_mid - 1
    elif binary_search_running:
        binary_search_running = False


def draw_binary_search():
    global binary_scroll_offset, binary_bar_width

    TITLE_HEIGHT = 60
    ANIMATION_HEIGHT = 250
    PSEUDO_START_Y = TITLE_HEIGHT + ANIMATION_HEIGHT + 20
    PSEUDO_AREA_HEIGHT = HEIGHT - PSEUDO_START_Y

    SCREEN.fill(WHITE)

    # Title
    title_surface = title_font.render("Binary Search", True, TITLE_TEXT_COLOR)
    SCREEN.blit(title_surface, (WIDTH // 2 - title_surface.get_width() // 2, 10))

    # Bars
    padding = 100
    available_width = WIDTH - 2 * padding
    binary_bar_width = available_width // binary_num_bars
    left_margin = padding
    animation_top = 100

    max_val = max(binary_array) if binary_array else 1
    for idx, val in enumerate(binary_array):
        bar_height = int(val / max_val * ANIMATION_HEIGHT)
        x = left_margin + idx * binary_bar_width
        y = animation_top + ANIMATION_HEIGHT - bar_height

        color = BLUE
        if idx == binary_mid and binary_search_running:
            color = (255, 165, 0)  # orange for current mid
        elif idx == binary_found_index:
            color = (0, 255, 0)  # green if found
        pg.draw.rect(SCREEN, color, (x, y, binary_bar_width - 2, bar_height))

    # Target value text
    target_text = font.render(f"Target Value: {binary_target}", True, (0, 0, 0))
    SCREEN.blit(target_text, (10, TITLE_HEIGHT))

    # Pseudocode area
    pseudo_surface = pg.Surface((WIDTH, PSEUDO_AREA_HEIGHT))
    pseudo_surface.fill((240, 240, 240))

    line_height = 28
    for idx, line in enumerate(binary_search_text):
        y = idx * line_height - binary_scroll_offset
        if -line_height < y < PSEUDO_AREA_HEIGHT:
            rendered = font.render(line, True, (0, 0, 0))
            pseudo_surface.blit(rendered, (20, y))
    SCREEN.blit(pseudo_surface, (0, PSEUDO_START_Y))

    # Back button
    back_btn.draw(SCREEN)